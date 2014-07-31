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
* 0.5.0 2014-07-31 Support for rbc-tools 0.1, the command line client for managing RedBridge Cloud.

* 0.4.10 2014-06-16 Added more Cloudstack object classes

* 0.4.9 2014-06-12 Added more Cloudstack object classes

* 0.4.8 2014-06-06 Packaging fixes

* 0.4.2 2014-06-06 Packaging fixes

* 0.4.1 2014-06-06 Fix a few bugs in the package includes and install_requires

* 0.4.0 2014-06-06 Initial release
