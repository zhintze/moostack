# Simple Voice Chat - Server Setup Guide

**Mod Version:** 2.6.8
**Minecraft Version:** 1.21.1 NeoForge
**Wiki:** https://modrepo.de/minecraft/voicechat/wiki/server_setup

## Overview

Simple Voice Chat uses a **separate UDP port** (not the Minecraft server port) for voice communication. This requires additional network configuration beyond standard Minecraft server setup.

## Quick Start

1. Install `voicechat-neoforge-1.21.1-2.6.8.jar` on both server and all clients
2. Open **UDP port 24454** on the server
3. Start the server - config file generates automatically
4. Test with `/voicechat test <playername>`

## Port Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| Protocol | UDP | Voice chat uses UDP, not TCP |
| Port | 24454 | Configurable in server config |

**Config file location:** `config/voicechat/voicechat-server.properties`

Key settings:
```properties
port=24454
bind_address=
max_voice_distance=48.0
```

## Firewall Setup by Environment

### VPS / Dedicated Server
```bash
# UFW (Ubuntu/Debian)
sudo ufw allow 24454/udp

# firewalld (RHEL/Fedora)
sudo firewall-cmd --permanent --add-port=24454/udp
sudo firewall-cmd --reload

# iptables
sudo iptables -A INPUT -p udp --dport 24454 -j ACCEPT
```

### Home/Local Network
1. Open UDP 24454 in your machine's local firewall
2. Configure port forwarding in your router:
   - External port: 24454
   - Internal port: 24454
   - Protocol: UDP
   - Internal IP: Your server machine's local IP
3. When connecting locally, use the server's local IP or `localhost`

### Docker
Add to your docker-compose.yml:
```yaml
ports:
  - "25565:25565"
  - "24454:24454/udp"  # Voice chat
```

### Pterodactyl Panel
1. Navigate to **Servers > Build Configuration > Allocation Management**
2. Assign port 24454 to the server
3. In **Settings > Nodes > Allocation**, add allocation with server IP and port 24454

## Testing Connection

### In-Game Test
```
/voicechat test <playername>
```
This sends a test audio packet to verify the connection.

### Important Notes
- Standard port checking tools **do not work** for UDP voice chat
- UDP is connectionless - requires the application to respond
- Use the in-game test command for verification

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Players can't hear each other | Check UDP 24454 is open, not just TCP |
| Voice works locally but not remotely | Check router port forwarding |
| Intermittent connection | Check firewall isn't rate-limiting UDP |
| "Connecting to server" stuck | Server port not reachable - verify firewall/NAT |

## Client Controls

Default keybinds (configurable):
- `V` - Push to talk
- `M` - Open voice chat settings
- `G` - Toggle microphone mute

## Additional Resources

- Full wiki: https://modrepo.de/minecraft/voicechat/wiki
- Server config options: https://modrepo.de/minecraft/voicechat/wiki/server_config
- Self-hosted guide: https://modrepo.de/minecraft/voicechat/wiki/server_setup_self_hosted
- Proxy setup: https://modrepo.de/minecraft/voicechat/wiki/server_setup_proxy
