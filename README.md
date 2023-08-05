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


 
## reportingIssuesImport.py:
Using selenium to get around a capcha issue, we can obtain a small number of the issuers in a CSV file



