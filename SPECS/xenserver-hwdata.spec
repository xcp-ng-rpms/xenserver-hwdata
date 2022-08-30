%global package_speccommit ae7e34038161871d5f9f9ff17fe56402f1784a56
%global package_srccommit v20210516
Name: xenserver-hwdata
Summary: Additional hardware identification and configuration data
Version: 20210516
Release: 1%{?xsrel}%{?dist}
License: GPLv2+
Group: System Environment/Base
Source0: xenserver-hwdata.tar.gz

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: hwdata

%description
Additional (more up-to-date) hardware identification and configuration data.

%prep
%autosetup -p1

%build
# nothing to build

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- hwdata
if [ -f /usr/share/hwdata/pci.ids ]; then
  mv /usr/share/hwdata/pci.ids /usr/share/hwdata/pci.ids.rpmsave
fi
ln -sf pci.ids.d/pci.ids /usr/share/hwdata

%files
%defattr(-,root,root)
/usr/share/hwdata/pci.ids.d/pci.ids
