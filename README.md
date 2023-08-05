# SEDARPlus
Programmatic access to the CSA's new filing/data access system, Sedar+


##
The difference between the origional Sedar and Sedar+ are:
- No longer require capcha to view documents on Sedar+
- A list of entities is available for export on Sedar+
- The modern design of SEDAR+ is more usable


That does not mean that SEDAR+ is anything close to the elegance of EDGAR. The drawbacks:
- All SEDAR+ are still PDF's.
- SEDAR+ is significantly slower than SEDAR
- The file that is exported is limited to 2,030 records, while there are over 10,000 filers
- There is no mapping file available, so unlike the convenient CIK's EDGAR uses, you must download the entire factset for SEDAR+. 
- The CDN configuration is abysmal. It takes close to 1 minute to download a 400kb file (this should take less than 10 seconds)


I have been able to grab all of the profiles from SEDAR in the past, it took hours to run and even with a limit of one request per .2 seconds the site went offline twice. It is entirely possible that SEDAR+ is even less usable as a developer, if it takes more than a couple hours to execute a program to capture every company profile, then it is not suitable for individial developers to scrape sedar: it would be too slow to keep up to date with new filers.
 
## reportingIssuesImport.py:
The first thing I notice: I need to solve a capcha if i take the traditional route of using the requests library. 
Instead, I use selenium in a way it was not supposed to be used, and it has proven excellent at bypasing any of the checks for bots.



