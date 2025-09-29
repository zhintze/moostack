#!/usr/bin/env python3
"""
Minecraft Memory Profiler
Monitors memory usage and provides optimization recommendations
"""

import psutil
import time
import json
import sys
from datetime import datetime
from pathlib import Path

class MinecraftMemoryProfiler:
    def __init__(self, minecraft_dir="/home/keroppi/Development/Minecraft/mooStack"):
        self.minecraft_dir = Path(minecraft_dir)
        self.log_file = self.minecraft_dir / "memory_profile.json"
        self.running = False
        
    def get_minecraft_processes(self):
        """Find all Minecraft-related processes"""
        minecraft_procs = []
        for proc in psutil.process_iter(['pid', 'name', 'cmdline', 'memory_info', 'cpu_percent']):
            try:
                cmdline = ' '.join(proc.info['cmdline']) if proc.info['cmdline'] else ""
                if any(keyword in cmdline.lower() for keyword in ['minecraft', 'java', 'gradle', 'moostack']):
                    if 'java' in proc.info['name'].lower() or 'minecraft' in cmdline.lower():
                        minecraft_procs.append(proc)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return minecraft_procs
    
    def get_memory_stats(self):
        """Get comprehensive memory statistics"""
        system_memory = psutil.virtual_memory()
        minecraft_procs = self.get_minecraft_processes()
        
        total_minecraft_memory = 0
        process_details = []
        
        for proc in minecraft_procs:
            try:
                memory_info = proc.memory_info()
                memory_mb = memory_info.rss / (1024 * 1024)  # Convert to MB
                total_minecraft_memory += memory_mb
                
                process_details.append({
                    'pid': proc.pid,
                    'name': proc.info['name'],
                    'memory_mb': round(memory_mb, 1),
                    'cpu_percent': proc.cpu_percent()
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        return {
            'timestamp': datetime.now().isoformat(),
            'system_memory': {
                'total_gb': round(system_memory.total / (1024**3), 2),
                'available_gb': round(system_memory.available / (1024**3), 2),
                'used_percent': system_memory.percent
            },
            'minecraft_memory': {
                'total_mb': round(total_minecraft_memory, 1),
                'process_count': len(minecraft_procs),
                'processes': process_details
            }
        }
    
    def analyze_memory_usage(self, stats):
        """Analyze memory usage and provide recommendations"""
        recommendations = []
        minecraft_mb = stats['minecraft_memory']['total_mb']
        system_used_percent = stats['system_memory']['used_percent']
        
        # Memory usage analysis
        if minecraft_mb > 9000:
            recommendations.append({
                'level': 'CRITICAL',
                'issue': 'Minecraft using >9GB memory',
                'recommendation': 'Reduce -Xmx to 8G, optimize mod configurations',
                'potential_savings': '1-2GB'
            })
        elif minecraft_mb > 7000:
            recommendations.append({
                'level': 'WARNING', 
                'issue': 'Minecraft using >7GB memory',
                'recommendation': 'Apply mod optimizations, tune GC settings',
                'potential_savings': '500MB-1GB'
            })
        
        # System memory pressure
        if system_used_percent > 90:
            recommendations.append({
                'level': 'CRITICAL',
                'issue': f'System memory usage at {system_used_percent}%',
                'recommendation': 'Reduce Minecraft memory allocation or close other applications',
                'potential_savings': 'System stability'
            })
        
        # Process analysis
        if stats['minecraft_memory']['process_count'] > 3:
            recommendations.append({
                'level': 'INFO',
                'issue': f"{stats['minecraft_memory']['process_count']} Minecraft processes running",
                'recommendation': 'Check for duplicate instances or gradle daemons',
                'potential_savings': '200-500MB per extra process'
            })
        
        return recommendations
    
    def generate_optimization_report(self, stats_history):
        """Generate detailed optimization report"""
        if not stats_history:
            return "No data available for analysis"
        
        latest_stats = stats_history[-1]
        recommendations = self.analyze_memory_usage(latest_stats)
        
        report = f"""
=== MINECRAFT MEMORY OPTIMIZATION REPORT ===
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

CURRENT MEMORY USAGE:
- Minecraft: {latest_stats['minecraft_memory']['total_mb']:.1f}MB
- System: {latest_stats['system_memory']['used_percent']:.1f}% used
- Available: {latest_stats['system_memory']['available_gb']:.1f}GB

OPTIMIZATION RECOMMENDATIONS:
"""
        
        for i, rec in enumerate(recommendations, 1):
            report += f"""
{i}. [{rec['level']}] {rec['issue']}
   → {rec['recommendation']}
   → Potential savings: {rec['potential_savings']}
"""
        
        # Memory trend analysis
        if len(stats_history) > 1:
            memory_trend = []
            for stats in stats_history[-5:]:  # Last 5 measurements
                memory_trend.append(stats['minecraft_memory']['total_mb'])
            
            avg_memory = sum(memory_trend) / len(memory_trend)
            latest_memory = memory_trend[-1]
            
            if latest_memory > avg_memory * 1.1:
                report += f"""
MEMORY LEAK DETECTION:
⚠️  Memory usage trending upward (current: {latest_memory:.1f}MB, avg: {avg_memory:.1f}MB)
   → Consider restarting the game or running garbage collection
"""
        
        return report
    
    def monitor(self, duration_minutes=60, interval_seconds=30):
        """Monitor memory usage for specified duration"""
        print(f"Starting memory monitoring for {duration_minutes} minutes...")
        print(f"Sampling every {interval_seconds} seconds")
        
        stats_history = []
        end_time = time.time() + (duration_minutes * 60)
        
        try:
            while time.time() < end_time:
                stats = self.get_memory_stats()
                stats_history.append(stats)
                
                # Print current status
                minecraft_mb = stats['minecraft_memory']['total_mb']
                system_percent = stats['system_memory']['used_percent']
                print(f"[{datetime.now().strftime('%H:%M:%S')}] "
                     f"Minecraft: {minecraft_mb:.1f}MB | System: {system_percent:.1f}% | "
                     f"Processes: {stats['minecraft_memory']['process_count']}")
                
                time.sleep(interval_seconds)
                
        except KeyboardInterrupt:
            print("\nMonitoring interrupted by user")
        
        # Save data and generate report
        with open(self.log_file, 'w') as f:
            json.dump(stats_history, f, indent=2)
        
        report = self.generate_optimization_report(stats_history)
        print(report)
        
        # Save report
        report_file = self.minecraft_dir / "memory_optimization_report.txt"
        with open(report_file, 'w') as f:
            f.write(report)
        
        print(f"\nData saved to: {self.log_file}")
        print(f"Report saved to: {report_file}")
        
        return stats_history
    
    def quick_check(self):
        """Quick memory usage check"""
        stats = self.get_memory_stats()
        recommendations = self.analyze_memory_usage(stats)
        
        print("=== QUICK MEMORY CHECK ===")
        print(f"Minecraft Memory: {stats['minecraft_memory']['total_mb']:.1f}MB")
        print(f"System Memory: {stats['system_memory']['used_percent']:.1f}% used")
        print(f"Processes: {stats['minecraft_memory']['process_count']}")
        
        if recommendations:
            print("\nRECOMMENDATIONS:")
            for rec in recommendations:
                print(f"[{rec['level']}] {rec['recommendation']}")
        else:
            print("\n✅ Memory usage looks good!")

def main():
    profiler = MinecraftMemoryProfiler()
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 memory_profiler.py check          - Quick memory check")
        print("  python3 memory_profiler.py monitor [min]  - Monitor for X minutes (default 60)")
        return
    
    command = sys.argv[1].lower()
    
    if command == 'check':
        profiler.quick_check()
    elif command == 'monitor':
        duration = int(sys.argv[2]) if len(sys.argv) > 2 else 60
        profiler.monitor(duration_minutes=duration)
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()