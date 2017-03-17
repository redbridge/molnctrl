=========================================
molnctrl - A Cloudstack python API client
=========================================

This is molnctrl a simple python Cloudstack API library.

Usage::

    import molnctrl
    csapi = molnctrl.Initialize("apikey", "api_secret", api_host='cloud.fqdn')
    accounts = csapi.list_accounts()

Changelog
=========
* 0.7.6 2017-03-17 Futurize

* 0.7.5 2017-01-25 Fix stupid error in 0.7.3

* 0.7.4 2017-01-25 Minor bug fix

* 0.7.3 2106-09-28 Actually fix import error

* 0.7.2 2106-09-27 Fix import error

* 0.7.1 2016-04-25 Fix requirements

* 0.7.0 2016-04-25 Modernized to use six (for Python 3 compatibility)

* 0.6.0 2015-02-10 Add support for POST

* 0.5.1 2014-09-30 Remove verify=false in requests

* 0.5.0 2014-07-31 Support for rbc-tools 0.1, the command line client for managing RedBridge Cloud.

* 0.4.10 2014-06-16 Added more Cloudstack object classes

* 0.4.9 2014-06-12 Added more Cloudstack object classes

* 0.4.8 2014-06-06 Packaging fixes

* 0.4.2 2014-06-06 Packaging fixes

* 0.4.1 2014-06-06 Fix a few bugs in the package includes and install_requires

* 0.4.0 2014-06-06 Initial release
