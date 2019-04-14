phyweb
========

[![Build Status](https://travis-ci.org/buaa-2016/phyweb.svg?branch=master)](https://travis-ci.org/buaa-2016/phyweb)
[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
[![Badge](https://img.shields.io/badge/link-996.icu-%23FF4D5B.svg)](https://996.icu/#/en_US)

A physical lab report generating platform.

[Click here to see this website!](http://114.115.142.227)

Build & Run
--------

See [this post](https://www.zybuluo.com/y3667931/note/1447675).

Deployment
--------

We have already set up a deployment script in the `deploy.sh`. If you finished building without any error, you can deploy this app on the server simply by the command below:

```bash
bash depoly.sh          # run the deployment script
```

This script will automatically add a service to `/etc/init.d/`, and start the service by `service phyweb start`. You can furtherly use below commands to start or stop the service:

```bash
service phyweb status   # check running status
service phyweb start    # start a background service
service phyweb stop     # stop service
service phyweb restart  # restart service
```

License
--------

[Anti-996 License](https://github.com/996icu/996.ICU/blob/master/LICENSE)


