Gyokuro LLC                                           Patrick Coleman 2020/12/16

Title: SaltyMicro Project Outline 
Author: Patrick Coleman 
Created: December 16th, 2020
Updated: August 3rd, 2021

<b style="color: white">Introduction</b>  
     SaltyMicro  is  a   suite  of  micro-services  intended  to gather,   save,
     predict and display data from the popular website https://www.SaltyBet.com.
      The suite  is intended to be comprised  of 4 programs, although only 3 are
      currently in development.

     Until this project, I was used to creating large monolithic programs. After
     reading  about containerization  and microservice  architecture, I  created
     this project to  explore some new design methods and  tools; namely, Docker
     and custom APIs.

<b style="color: white">What is SaltyBet?</b> 
     For those unaware  (most people), SaltyBet is  akin to a virtual version of
     The Ultimate Fighting Championship. At www.SaltyBet.com is a live stream of
     virtual, AI-controlled, fan-made  characters duking  it out 24/7. Thousands
     of spectators tune in daily  to  watch  fights and bet fake-money (known as
     "salt")  on their  favorite characters. There  are thousands of characters;
     from Darth Vader to Ronald McDonald, you never know who will be victorious.

     If your familiar with fighting games like Mortal Kombat, Street Fighter, or
     Tekken, SaltyBet  will look  quite familiar.  SaltyBet is  built on  the 2D
     fighting  game engine  Mugen. Released  in 1999  by Elecbyte,  Mugen gained
     notoriety by allowing  players to create and import their  own fighters. At
     some  point  Salty,  Saltybet's  creator,  saw  the  potential  in  Mugen's
     community and created SaltyBet where the Mugen community could compare each
     others custom fighters in front of a live audience.

<b style="color: white">SaltyMicro</b>  
     SaltyMicro  is  a  suite of  programs  which  collect,  save, predict,  and
     display data from  SaltyBet. I  plan to have 4  programs, however presently
     there are  three: SaltyBoutObserver(SBO), SaltyDataController(SDC), and the
     SaltyUserInterface(SUI). The SBO watches  SaltyBet and  scrapes data  about
     every fight. This data is then sent to  the SDC for storage and processing.
     Lastly,  the SUI requests information from the SDC to display for the user.
     Below is a diagram:

<p style="color: white">  
                         +----------+
                         | saltybet |   1. a fight ends.
                         +----+-----+
                              |
                           +--V--+
                           | SBO |      2. SBO sends fight data to SDC.
                           +--+--+
               +---+          |
               |   |<------+--V--+
               |SQL|       | SDC |      3. SDC formats data and saves it.
               |   |------>+--+--+
               +---+          |
                           +--V--+
                           | SUI |      4. SUI displays information for users.
                           +-----+
</p>

<b style="color: white">SaltyBoutObserver</b> 
     The  SaltyBoutObserver(SBO) is  part of  the SaltyMicro software suite. Its
     function is to observe  SaltyBet. When a bout ends, SBO will scrape data of
     the bout and  send it  to the SDC for further processing.  SBO will  gather
     information such as:fighter names, bets, winners, matchmaking mode, and the
     date. When this information reaches the SDC it will be processed further to
     reveal additional  information. Navigating  to: [sbo-url]/api/v1/help  will
     display an updated list of API options.

     ENVIRONMENT VARIABLES:   
                    SBO_HOST=[sbo-ip]
                    SBO_PORT=[sbo-port]
                    SBO_SDC_URL=[sdc-url] 
                    SBO_SALTY_URL='https://www.saltybet.com/state.json'

<b style="color: white">SaltyDataController</b>>
     The SaltyDataController (SDC) is part of the SaltyMicro software suite. Its
     function is to process information from the SBO and store it in a database.
     This is the brains of the SaltyMicro suite. When the SBO sends data  to the
     SDC,  it  will  insert a  new  row into  the  BOUTS table in  the database.
     The  BOUTS table  contains fighter-names,  bets,  winner, matchmaking-type,
     date, and whether the bout was an upset (the underdog won).

     In addition the  SDC will scrape out  the Fighters and try to  find them in
     the FIGHTERS table. If the fighter is already in the database, the SDC will
     update their stats with  new information acquired  from  their recent bout.
     The  FIGHTERS  table  contains  a  lot  of  information  including  obvious
     information  like the  fighter's  name, along  with  some more  interesting
     information like win/loss record, record  winning streak, number of upsets,
     and an ELO ranking.

     The ELO  ranking system  is similar  to the one  used to  rank professional
     chess players in the  FIDE World Chess Federation. It uses a  K value of 40
     and a  baseline ELO  of 2000 by  default. This means  a fighter  never seen
     before by the SDC will have an elo of 2000.

     The SDC  has a  robust API, allowing  external devices to  ask the  SDC for
     data. FIGHTERS and BOUTS can be requested  based on any field in the table.
     No custom SQL can be passed to  the database, all queries are hard-coded in
     the SDC and thus data must be asked for through the SDC API. Navigating to:
     [sdc-url]/api/v1/help will display an updated list of API options. All data
     returned from the SDC is in json format.

     ENVIRONMENT VARIABLES:
                    SDC_HOST=[sdc_ip]
                    SDC_PORT=[sdc_port]
                    SDC_SQL_HOST=[sql-ip]
                    SDC_SQL_PORT=[sql_port]
                    SDC_SQL_USER-[sql_user]
                    SDC_SQL_SECRET=[sql_secret]
                    SDC_SQL_DEFAULT_DB=[sql_default_db]
                    SDC_SQL_DB=[sql_db]
                    SDC_SQL_DROP=[true, false]
                    
<b style="color: white">SaltyUserInterface</b> 
     The SaltyUserInterface (SUI) is  a dashboard, more  like a  command center,
     for the SaltyMicro  suite.  SUI  has  pages  which  display  all  sorts  of
     information;  including   the  latest  bouts,  newest  fighters,  and   the
     configurations  of  SDC, SBO, and  SUI for troubleshooting purposes. If the
     SaltyMicro suite is not  functioning correctly, the  Configurations  tab of
     SUI  will likely  help  resolve  the issue. In addition, SUI has  pages for
     browsing through all the Fighters and Bouts recorded by the SDC.

     All the information displayed in SUI  is retrieved from the SDC through GET
     requests. The SDC  sends information in json format and  SUI will format it
     to be more pretty and display it to the user.
                         
     ENVIRONMENT VARIABLES:
                    SUI_HOST=[sui-ip]
                    SUI_PORT=[sui-port]
                    SUI_SBO_URL=[sbo_url]
                    SUI_SDC_URL=[sdc_url]
                    
<b style="color: white">Environment</b> 
     The  environment  is  flexible. All three programs are  designed to  run in
     essentially limitless configurations as long  as the  environment variables
     are configured correctly.

     I have configured the SDC, SBO and PostgreSQL database to run in containers
     behind an NGINX reverse-proxy to perform proxy-pass based on the entry url.
     I  run  this configuration  on  a  lightweight alpine-linux  machine.  With
     docker-compose, I can deploy this NGINX, SDC, SBO, PostgreSQL configuration
     on any linux machine in about 30  seconds. Docker is truly an amazing piece
     of technology! Below is a diagram:
        
<p style="color: white">                    
   +-------------------------------------+
   |Linux VM (SBO, SDC, and PostgreSQL)  |
   |                                     |
   |    +---------------------------+    |
   |    |Docker Network             |    |
   |    |                           |    |  +-----------------------------+
   |    |          +-----+          |    |  | Linux VM (SUI)              |
   |    |          |NGINX|          |    |  |   +---------------------+   |
   |    |          +-----+          |    |  |   |Docker Network       |   |
   |    |          |     |          |    |  |   |                     |   |
   |    |       +--++   ++--+       |    |  |   |                     |   |
   |    |       |SDC|   |SBO|       |    |  |   |       +-----+       |   |
   |    |       +-+-+   +---+       |    |  |   |       |NGINX|       |   |
   |    |         |                 |    |  |   |       +--+--+       |   |
   |    |       +-+-+               |    |  |   |          |          |   |
   |    |       |SQL|               |    |  |   |        +-+-+        |   |
   |    |       +---+               |    |  |   |        |SUI|        |   |
   |    |                           |    |  |   |        +---+        |   |
   |    +---------------------------+    |  |   |                     |   |
   |                                     |  |   +---------------------+   |
   |                                     |  |                             |
   +-------------------------------------+  +-----------------------------+

################################################################################

                       Below are some dataflow examples:
     
################################################################################
     
     +------------------+-----------------------------+-------------------+
     |                  +-----------------------------+                   |
     |                  | A User Requests Information |                   |
     |                  +-----------------------------+                   |
     |                                                                    |
     |                             +----+   +---+   +---+   +---+   +---+ |
     | 1. a USER requests data     |USER|   |SUI|   |SBO|   |SDC|   |SQL| |
     |    from the SUI.            +-+--+   +-+-+   +-+-+   +-+-+   +-+-+ |
     |                               |        |       |       |       |   |
     | 2. SUI forwards the request   |   1    |       |       |       |   |
     |    to the SDC using the SDC   +------->|       |       |       |   |
     |    API.                       |        |   2   |       |       |   |
     |                               |        +-------+------>|       |   |
     | 3. SDC queries the database   |        |       |       |   3   |   |
     |    to retrieve information.   |        |       |       +------>|   |
     |                               |        |       |       |   4   |   |
     | 4. The database replies with  |        |       |       |<------+   |
     |    the requested rows.        |        |       |   5   |       |   |
     |                               |        |<------+-------+       |   |
     | 5. SDC formats the data into  |        |       |       |       |   |
     |    json and delivers it to    |    6   |       |       |       |   |
     |    SUI                        |<-------+       |       |       |   |
     |                               |        |       |       |       |   |
     | 6. SUI presents the data to   |        |       |       |       |   |
     |    the USER.                  |        |       |       |       |   |
     |                               |        |       |       |       |   |
     |                               |        |       |       |       |   |
     |                               |        |       |       |       |   |
     |                               v        v       v       v       v   |
     |                                                                    |
     +--------------------------------------------------------------------+
	
################################################################################

     +------------------------+------------------+------------------------+
     |                        +------------------+                        |
     |                        | A New Fight Ends |                        |
     |                        +------------------+                        |
     |                                                                    |
     |                             +----+   +---+   +---+   +---+   +---+ |
     |                             | SB |   |SUI|   |SBO|   |SDC|   |SQL| |
     |                             +-+--+   +-+-+   +-+-+   +-+-+   +-+-+ |
     |                               |    1   |       |       |       |   |
     | 1. SBO checks SaltyBet for    |<-------+-------+       |       |   |
     |    new fight data.            |        |       |       |       |   |
     |                               |    2   |       |       |       |   |
     | 2. SBO replies with the       +--------+------>|       |       |   |
     |    latest fight data.         |        |       |       |       |   |
     |                               |        |       |   3   |       |   |
     | 3. If the fight is concluded  |        |       +------>|       |   |
     |    SBO will send the data to  |        |       |       |       |   |
     |    SDC for processing and     |        |       |       |   4   |   |
     |    storage.                   |        |       |       +------>|   |
     |                               |        |       |       |       |   |
     | 4. SDC formats the data,      |        |       |       |       |   |
     |    calculates elo and sends   |        |       |       |       |   |
     |    it to the database for     |        |       |       |       |   |
     |    storage.                   |        |       |       |       |   |
     |                               |        |       |       |       |   |
     |                               |        |       |       |       |   |
     |                               |        |       |       |       |   |
     |                               |        |       |       |       |   |
     |                               |        |       |       |       |   |
     |                               v        V       V       V       V   |
     +--------------------------------------------------------------------+

################################################################################
</p>

     None  of the  programs require  the  others to  run. They  simply wait  for
     requests.  If the  SBO goes  down it  will  not impact  the SDC  or SUI  at
     all.  In  fact, SUI  will  report  it has  lost  contact  with the  SBO  in
     the  configurations tab.  Once  the SBO  is back  online,  SUI will  regain
     connectivity.

     Likewise if the SDC goes offline, it  will not hurt SBO or SUI. However all
     the data the SBO  tries to send to the SDC will be  lost. This means if the
     SDC goes  down the  database will not  be able to  be accessed  or updated.
     Again ,  this does not impact  the ability for  the SUI or SBO  to operate,
     however it does mean data will not be captured.

     SUI is simply a  viewport. If SUI goes offline, the rest  of the suite will
     continue to  operate. This means  data will still  be collected and  can be
     viewed directly through the SDC API, or once SUI is back online.

<b style="color: white">Warnings</b>
     This  project is  over a year  old  at this  point. When  I began designing
     this project, Most of my  experience was in Python; I had little experience
     with web development and zero experience with containerization. As a result
     there is undoubtedly many inefficiencies within the  SaltyMicro suite. This
     project will  likely be in development for years.  I'm constantly learning,
     and as I learn I make adjustments  to better optimize existing  systems and
     add new features.

<b style="color: white">Future Development</b> 
     As stated prior, I have many plans for new features:

     SaltyBot: Earlier, I alluded to a  fourth program. This program is intended
     to be a  automatic betting robot. The SaltyBot will  retrieve data from the
     SDC to  make fight predictions using  the ELO ranking system.  The SaltyBot
     will  create logs  of its  predictions  and transmit  them to  the SDC  for
     storage.

     Email/SMS Alerts: I plan  on adding a feature to SBO  that notifies me when
     particular fighters  are about to  fight. Since SaltyBet is  randomized, It
     can be difficult to catch a  fight between my favorite fighters. Having SBO
     monitoring pre-games  for particular fighters  and alerting me when  one is
     about to fight would be nice to have.

     Optimizations: I know my web development skills have improved a lot since I
     began writing SUI, as have my knowledge of python libraries. I intend to go
     back and review my  code and try to condense it as  much as possible. There
     are  also some  inefficiencies  in how  web-content is  served.  I plan  on
     optimizing this as well to reduce the time it takes to load content in SUI.
