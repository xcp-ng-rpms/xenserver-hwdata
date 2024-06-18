%global package_speccommit 3f209234410e6a0f027f3b61c3cd7185bd6ed568
%global package_srccommit v20240411
Name: xenserver-hwdata
Summary: Additional hardware identification and configuration data
Version: 20240411
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

%changelog
* Tue Apr 23 2024 Stephen Cheng <stephen.cheng@cloud.com> - 20240411-1
- CA-391652: Update pci.ids to version 2024.04.11
