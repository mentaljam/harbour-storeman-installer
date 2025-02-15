# Storeman Installer

**The Storeman Installer for SailfishOS performs the initial installation of the [Storeman OpenRepos client application](https://github.com/storeman-developers/harbour-storeman#readme). Storeman Installer selects, downloads and installs the correct variant of the Storeman application built for the CPU-architecture of the device and the installed SailfishOS release from the SailfishOS-OBS.**

### Background

Starting with version 0.2.9, Storeman is built by the help of the SailfishOS-OBS and initially installed by the Storeman Installer (or manually).  To update from Storeman <&nbsp;0.2.9 (requires SailfishOS ≥&nbsp;3.1.0), one should reinstall Storeman via the Storeman Installer.  After an initial installation of Storeman ≥&nbsp;0.3.0, further updates of Storeman will be performed within Storeman, as usual.

The Storeman Installer works on any SailfishOS release ≥&nbsp;3.1.0 and all three supported CPU-architectures (aarch64, armv7hl and i486).  The current Storeman Installer RPM can be obtained from its ["latest release" page at GitHub](https://github.com/storeman-developers/harbour-storeman-installer/releases/latest) and [OpenRepos.net](https://openrepos.net/content/olf/storeman-installer).

RPMs of [older Storeman releases are also available at OpenRepos](https://openrepos.net/content/olf/storeman-legacy), e.g. v0.1.8 which works on SailfishOS 2.2.1 and may work on older SailfishOS 2 releases.

### Important notes

* If you experience issues with Storeman Installer, please take a look at its log-file `/var/log/harbour-storeman-installer.log.txt`.  If that does not reveal to you what is going wrong, please check first if an issue report describing this issue is [already filed at GitHub](https://github.com/storeman-developers/harbour-storeman-installer/issues), then you might file a new issue report there and attach the log-file to it, or enhance an extant bug report.
* If you experience issues when installing, removing or updating packages after a SailfishOS upgrade, try running `devel-su pkcon refresh` in a terminal app.
* When Storeman Installer fails to install anything (i.e. a minute after installing it the icon of Storeman has not appeared on the launcher / desktop), most likely the preceding or the following bullet point is the reason.
* Before software can be build for a new SailfishOS release at the SailfishOS-OBS, Jolla must create a [corresponding "download on demand (DoD)" OBS-repository](https://build.sailfishos.org/project/subprojects/sailfishos).  Before that is employed by Jolla, Storeman's download repository for this new SailfishOS release will usually be mapped to the prior SailfishOS release by [its OBS-meta-configuration](https://build.sailfishos.org/project/meta/home:olf:harbour-storeman), in hope that there is no change in the new SailfishOS release which breaks Storeman; if there is, please report that soon at [Storeman's issue tracker](https://github.com/storeman-developers/harbour-storeman/issues).
* Disclaimer: Storeman and its installer may still have flaws, kill your kittens or break your SailfishOS installation!  Although this is very unlikely after years of testing by many users, new flaws may be introduced in any release (as for any software).  Mind that the license you implicitly accept by using Storeman or Storeman Installer excludes any liability.

### Installation instructions

* Initial installation without having Storeman already installed
  1. Enable "System → Security → Untrusted software → Allow untrusted software" in the SailfishOS Settings app.
  2. Download the current Storeman Installer RPM from its ["latest release" page at GitHub](https://github.com/storeman-developers/harbour-storeman-installer/releases/latest) or [OpenRepos.net](https://openrepos.net/content/olf/storeman-installer).
  3. Tap on the "File downloaded" notification on your SailfishOS device or select the downloaded RPM file in a file-manager app and choose "Install" in its pulley menu; then confirm the installation.
  4. Preferably disable "Allow untrusted software" again.

* Installation via Storeman (i.e. updating from Storeman <&nbsp;0.2.9)
  * <sup>If you have [olf's repository at OpenRepos](https://openrepos.net/user/5928/programs) enabled, *Storeman Installer* should be offered as an update candidate for the outdated *Storeman* installed: Just accept this offer.<br />Otherwise:</sup>
  1. Search for *Installer*.
  2. Select the *Storeman Installer* by *olf*.
  3. Enable olf's repository in the top pulley menu.
  4. Install *Storeman Installer*.

### Features of Storeman Installer

* The Storeman Installer is automatically removed ("uninstalled") when Storeman is being installed.
* [Storeman Installer 1.3.1](https://github.com/storeman-developers/harbour-storeman-installer/releases/tag/1.3.1) and all later versions are offered as an update candidate for Storeman, if an RPM repository is enabled, which offers the *harbour-storeman-installer* package and Storeman (*harbour-storeman* package) <&nbsp;0.2.99 is already installed.
* Installing [Storeman Installer 1.3.1](https://github.com/storeman-developers/harbour-storeman-installer/releases/tag/1.3.1) and all later versions also automatically removes an installed Storeman (*harbour-storeman* package) <&nbsp;0.2.99, which eliminates the former necessity to manually remove ("uninstall") an old Storeman. 
* [Storeman Installer 1.3.8](https://github.com/storeman-developers/harbour-storeman-installer/releases/tag/1.3.8) and all later versions create a persistent log-file `/var/log/harbour-storeman-installer.log.txt`.
* Storeman Installer 2 runs "unattended": I.e. without any manual steps, after its installation has been triggered, until Storeman is installed.
* Storeman Installer is slow, because it calls `pkcon` two (releases before v1.3.8) to three times (releases from v[1.3.8](https://github.com/storeman-developers/harbour-storeman-installer/releases/tag/1.3.8) on), which acts quite slowly.  The minimal run time for Storeman Installer 2 is about 7 seconds, the typical run time is rather 10 seconds (measured from the moment Storeman Installer's installation is triggered, until Storeman is installed and its icon is displayed at the "launcher").  This is already a lot, but rarely the Packagekit daemon stalled (`packagekitd`, for which `pkcon` is just a command line front-end, communicating with the daemon via D-Bus) during heavy testing, which can be observed with the crude `pkmon` utility (`Ctrl-C` gets you out. :smiley:), so the Storeman Installer now tries to detect these "hangs" and to counter them: If that happens, its run time can be up to slightly more than 1 minute.  In the worst case a stalled PackageKit daemon (and with it its `pkcon` client process(es)) stalls Storeman Installer, until the PackageKit daemon reaches its idle time out of 300 seconds (5 minutes; this could theoretically happen three times, resulting in a likely unsuccessful run time of more than 15 minutes).<br />
Also note that SailfishOS sometimes fails to show an icon of a freshly installed app on the launcher ("homescreen") until SailfishOS is rebooted (rsp. more precisely: Lipstick is restarted).
