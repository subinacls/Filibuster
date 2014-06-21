Filterbuster
============

Egress filter mapping application with additional functionality
Expanded from: https://www.trustedsec.com/files/egressbuster.zip

  [*] Commandline Usage: ...
  
    {Client}  term:$ python ./filterbuster.py client (config.file) (no/yes)
  
    {Server}  term:$ python ./filterbuster.py server (tcp/udp/both) (port) (no/yes)

  [-] Understanding the client: ....

  The client is configured via a ini file specified on the commandline. This file is parsed 
  and used within the applications logic to configure the scanning engine and load additional
  modules into the framework.
  
  [-] Client Configuration file: ...

  Below is a sample configuration file used by the application. As modules are introduced, this
  configuration file will obviously need expanding as required. The examples below expect some
  modification from the end user -

  
      [SectionOne]

        diagnostics: ( boolean )
        target: ( 127.0.0.1 / hostname / subdomain.domain.tla )
        types: ( connect )
        spoof: ( boolean )
        range: ( portlist.txt / 0-65535 )
        random: ( boolean )
        protocol: ( tcp / udp / icmp / etc / etc )
        consultant: ( your name )
        location: ( your location )
      
      [SectionTwo]
      
        sleep: ( static / random )
        nappy: ( number )
        dwell: ( number )
      
      [SectionThree]
      
        suppress: ( boolean )
        logging: ( boolean )
        logtype: ( txt / xml / csv / json )
        covert: ( boolean )

  
  [-] Understanding the server: ....
  
  The server is threaded, bound to a single port and listens on all interfaces meaning all attempted 
  communications on the IP stack will be redirected to the server and it will answer the attempted 
  communication if specific criteria are meet. If these conditions are not fulfilled the server will 
  append any received data to a Contaminated file which can be used as an Honeypot of sorts.
  
  No information about the scanning results are logged onto the server with one exception,the
  Contamination log file which will not retain any information about the client and their egress rules.
  
  There really is no actual configuration to the server other than commandline options. As the applications
  functionality expands this could change.
  
  [-] TODO list: ....

  MORE SCAPY
  IPv6 Support
  More protocol testing
  More Covert / backchannel test
  Better Request handling
  FwKnop for remote administration
  IDS/IPS testing (sending known signatures)
    Modes:[
        silent.
        quiet.
        loud,
        OBVIOUS,
        OBNOXIOUS
    ]
    Send known shellcodes signatures
    Send known malware signatures
    Send known virus signatures
    Send known botnet signatures
    Send known bufferoverflow signatures
    Send clear text Personal Identifiable Information (PII) signatures
    Send Clear text Payment Card Industry (PCI) signatures
  Monitor and report activity on wire to identify other vectors of attack
  Covert tunnel proxy options
      
      
      
      
