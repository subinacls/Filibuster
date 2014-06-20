Filterbuster
============

Egress filter mapping application with additional functionality

  [*] Commandline Usage: ...
  
  {Client}  term:$ python ./filterbuster.py client [config.file]
  
  {Server}  term:$ python ./filterbuster.py server (tcp/udp/both) [port] (no/yes)

  [-] Understanding the client: ....

  The client is configured via a ini file specified on the commandline. This file is parsed 
  and used within the applications logic to configure the scanning engine and load additional
  modules into the framework.
  
  [-] Client Configuration file: ...

  Below is a sample configuration file used by the application. As modules are introduced, this
  configuration file will obviously need expanding as required. The examples below expect some
  modification from the end user -

  
      [SectionOne]
        
        target: (127.0.0.1 / hostname / subdomain.domain.tla)
        types: (connect/icmp/dns/ntp)
        spoof: (yes/no)
        range: (portlist.txt/0-65535)
        random: (True/False)
        protocol: (tcp/udp/icmp/etc/etc/)
        consultant: (your name)
        location: (your location)
      
      [SectionTwo]
      
        sleep: (static/random)
        nappy: (whole number)
        dwell: (whole number)
      
      [SectionThree]
      
        suppress: (True/False)
        logging: (True/False
        logtype: (txt/xml/csv/json)
        covert: (True/False)

  
  [-] Understanding the server: ....
  
  The server is threaded, bound to a single port and listens on all interfaces meaning all attempted 
  communications on the IP stack will be redirected to the server and it will answer the attempted 
  communication if specific criteria are meet. If these conditions are not fulfilled the server will 
  append any received data to a Contaminated file which can be used as an Honeypot of sorts.
  
  No information about the scanning results are logged onto the server with one exception,the
  Contamination log file which will not retain any information about the client and their egress rules.
  
  There really is no actual configuration to the server other than commandline options. As the applications
  functionality expands this could change.
  
      
      
      
      
      
      
      
      
