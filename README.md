python_npi-check
================

Python (2.x) version of HIPAA National Provider Identifier (NPI) checksum verification functions. 
The module contains two functions, getNPIchecksum() and NPIisGood().  

getNPIchecksum() calculates the Luhn checksum of a supplied 10- or 15-digit NPI from the first 9 or 14 digits. If 10 digit NPI is supplied, USA prefix of 80840 is assumed.

NPIisGood() uses getNPIchecksum to verify the checksum digit of the supplied NPI. If the checksum is valid it returns True, if invalid it returns False, and if the length or format of the supplied NPI are improper it returns a string with an error message.

This module was originally provided to and posted on the ClareEDI NPI resources page at https://www.claredi.com/download/npi_resources.php, but the link has been broken for some time and ClarEDI support informs me they have no plans to fix it.
