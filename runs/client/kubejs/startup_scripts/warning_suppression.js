// Warning Suppression Script
// Reduces mod-specific warnings and spam messages

console.log('=== Warning Suppression Script Loading ===')

// ===== SYSTEM PROPERTY SUPPRESSIONS =====

try {
    // Try to set system properties using Java's System class
    let System = Java.loadClass('java.lang.System')
    
    // Suppress Java AWT warnings (headless mode)
    System.setProperty('java.awt.headless', 'true')
    
    // Suppress file encoding warnings
    System.setProperty('file.encoding', 'UTF-8')
    System.setProperty('sun.stdout.encoding', 'UTF-8')
    System.setProperty('sun.stderr.encoding', 'UTF-8')
    
    // Suppress Netty warnings
    System.setProperty('io.netty.noUnsafe', 'true')
    System.setProperty('io.netty.tryReflectionSetAccessible', 'false')
    
    // Suppress reflection warnings
    System.setProperty('sun.reflect.debugModuleAccessChecks', 'false')
    
    // Suppress SSL/security warnings in development
    System.setProperty('com.sun.net.ssl.checkRevocation', 'false')
    System.setProperty('sun.security.ssl.allowUnsafeRenegotiation', 'true')
    
    console.log('Applied system property warning suppressions')
} catch (e) {
    console.log('Could not set system properties at runtime - consider setting via JVM args')
}

// ===== MOD-SPECIFIC SUPPRESSIONS =====

StartupEvents.init(event => {
    console.log('Applying mod-specific warning suppressions...')
    
    // Suppress common development warnings that clutter console
    try {
        // Configure logging levels programmatically where possible
        let loggerContext = Java.loadClass('org.apache.logging.log4j.LogManager')
        
        // This is a fallback - the main suppression happens via log4j2.xml
        console.log('Log4j configuration will be handled by log4j2.xml')
        
    } catch (e) {
        // Ignore if log4j classes aren't available yet
        console.log('Log4j not available during startup, relying on XML config')
    }
})

console.log('=== Warning Suppression Script Loaded ===')