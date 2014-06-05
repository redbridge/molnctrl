=========================================
molnctrl - A Cloudstack python API client
=========================================

This is molnctrl a simple python Cloudstack API library.

Usage:

    import molnctrl
    csapi = molnctrl.Initialize("apikey", "api_secret", api_host='cloud.fqdn')
    accounts = csapi.list_accounts()

Changelog
=========

* 0.4.1 2014-06-06 Fix a few bugs in the package includes and install_requires

* 0.4.0 2014-06-06 Initial release
