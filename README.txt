# Salty User Interface Redux!

After much consideration I have decided to revamp SUI. This is mainly because i have learned a 
lot in the past few days and believe I can make many improvements.

Most notably, I have removed logging entirely as it was about half the codebase and was a classic
example of bringing a sledgehammer to crack a nut.

I also got rid of pycharm and have been using this to experiemnt with VisualStudio Code.

# Config
in app.mnt is a file named config.txt it should look like the following:
{"l_addr": "0.0.0.0", "l_port": "50300", "sbo_url": "http://<fqdn>:<port>/api/v1/", "sdc_url": "http://<fqdn>:<port>/api/v1/"}
