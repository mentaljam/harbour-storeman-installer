Summary:        Storeman Installer for SailfishOS
License:        MIT
Name:           harbour-storeman-installer
Version:        1.3.0
Release:        1
Group:          System
URL:            https://github.com/storeman-developers/harbour-storeman-installer
Source0:        %{name}-%{version}.tar.bz2
Requires:       ssu
BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  sailfish-svg2png

%define localauthority_dir polkit-1/localauthority/50-local.d
%define hicolor_icons_dir  %{_datadir}/icons/hicolor

%description
Selects the correct variant of the Storeman OpenRepos client application built for the CPU-architecture of the device and the installed SailfishOS release.

# This description section includes metadata for SailfishOS:Chum, see
# https://github.com/sailfishos-chum/main/blob/main/Metadata.md
%if "%{?vendor}" == "chum"
PackageName: Storeman Installer for SailfishOS
Type: desktop-application
Categories:
 - Utilities
 - System
DeveloperName: Storeman Developers (mentaljam)
Custom:
  Repo: %{url}
Icon: %{url}/raw/master/harbour-storeman-installer.svg
Screenshots:
 - https://github.com/storeman-developers/harbour-storeman/raw/master/.xdata/screenshots/screenshot-screenshot-storeman-01.png
 - https://github.com/storeman-developers/harbour-storeman/raw/master/.xdata/screenshots/screenshot-screenshot-storeman-02.png
 - https://github.com/storeman-developers/harbour-storeman/raw/master/.xdata/screenshots/screenshot-screenshot-storeman-03.png
 - https://github.com/storeman-developers/harbour-storeman/raw/master/.xdata/screenshots/screenshot-screenshot-storeman-04.png
 - https://github.com/storeman-developers/harbour-storeman/raw/master/.xdata/screenshots/screenshot-screenshot-storeman-06.png
 - https://github.com/storeman-developers/harbour-storeman/raw/master/.xdata/screenshots/screenshot-screenshot-storeman-07.png
 - https://github.com/storeman-developers/harbour-storeman/raw/master/.xdata/screenshots/screenshot-screenshot-storeman-08.png
 - https://github.com/storeman-developers/harbour-storeman/raw/master/.xdata/screenshots/screenshot-screenshot-storeman-09.png
Url:
  Homepage: %{url}
  Help: %{url}/issues
  Bugtracker: %{url}/issues
%endif

%prep
%setup -q -n %{name}-%{version}

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 bin/%{name} %{buildroot}%{_bindir}/%{name}

install -d %{buildroot}%{_sharedstatedir}/%{localauthority_dir}
install %{localauthority_dir}/* %{buildroot}%{_sharedstatedir}/%{localauthority_dir}

for s in 86 108 128 172
do
  prof=${s}x${s}
  install -d %{buildroot}%{hicolor_icons_dir}/$prof/apps
  sailfish_svg2png -s 1 1 1 1 1 1 $s . %{buildroot}%{hicolor_icons_dir}/$prof/apps
done

# a. `desktop-file-install --help-install` states that the syntax is `-dir=`: To check, but seems to work without it.
# b. Just an idea to try: -m 755 | --mode=755 may be helpful for resolving issue #1
desktop-file-install --delete-original --dir %{buildroot}%{_datadir}/applications %{name}.desktop

%posttrans
ssu rr mentaljam-obs
rm -f /var/cache/ssu/features.ini
ssu ar harbour-storeman-obs 'https://repo.sailfishos.org/obs/home:/olf:/harbour-storeman/%%(release)_%%(arch)/'
ssu ur

%postun
ssu rr harbour-storeman-obs
rm -f /var/cache/ssu/features.ini
ssu ur

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_sharedstatedir}/%{localauthority_dir}/50-%{name}-packagekit.pkla
%{hicolor_icons_dir}/*/apps/%{name}.png

%changelog
* Sun Mar 13 2022 olf <https://github.com/Olf0> - 1.2.0-1
- Change group from users to ssu
- polkit: Limit allowed actions to the necessary ones
- Do not to call Bash
- desktop file: Only label languages by country code 
- Create bug-template.md / Create suggestion-template.md
- Create build.yml
- Update repository configuration
- Add URL: to spec file
- Update spec file
* Mon Sep  6 2021 Petr Tsymbarovich <petr@tsymbarovich.ru> - 1.1.0-1
- Update translations
* Sun Aug 22 2021 Petr Tsymbarovich <petr@tsymbarovich.ru> - 1.0.1-1
- Update translations
* Thu Aug 19 2021 Petr Tsymbarovich <petr@tsymbarovich.ru> - 1.0.0-1
- Initial release
