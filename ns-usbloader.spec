%global debug_package %{nil}

Name:           ns-usbloader
Version:        7.0
Release:        1%{?dist}
Summary:        Multi use tool for managing your Switch
License:        GPL-3.0-or-later
URL:            https://github.com/developersu/%{name}
BuildArch:      noarch

Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        99-%{name}.rules
Source2:        %{name}

Patch0:         %{name}-jar.patch
Patch1:         %{name}-desktop.patch

BuildRequires:  desktop-file-utils
BuildRequires:  java-devel
BuildRequires:  libappstream-glib
BuildRequires:  maven
BuildRequires:  systemd-rpm-macros

Requires:       jre-headless

%description
NS-USBloader is an Awoo Installer and GoldLeaf uploader of the NSPs (and other
files), RCM payload injector, application for split/merge files.

%prep
%autosetup -p1

%build
mvn -B -DskipTests clean package

%install
install -p -m644 -D target/%{name}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
install -p -m644 -D misc/freedesktop_entry/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -p -m644 -D misc/freedesktop_entry/%{name}.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg
install -p -m644 -D %{SOURCE1} %{buildroot}%{_udevrulesdir}/99-%{name}.rules
install -p -m755 -D %{SOURCE2} %{buildroot}%{_bindir}/%{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%license LICENSE
%doc README.md screenshots
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_javadir}/%{name}
%{_udevrulesdir}/99-%{name}.rules

%changelog
* Sun Oct 22 2023 Simone Caronni <negativo17@gmail.com> - 7.0-1
- First build.
