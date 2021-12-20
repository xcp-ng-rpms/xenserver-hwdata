Name: xenserver-hwdata
Summary: Additional hardware identification and configuration data
Version: 20210516
Release: 1%{?dist}
License: GPLv2+
Group: System Environment/Base

Source0: https://code.citrite.net/rest/archive/latest/projects/XS/repos/xs-hwdata/archive?at=v20210516&format=tar.gz&prefix=xenserver-hwdata-20210516#/xenserver-hwdata.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XS/repos/xs-hwdata/archive?at=v20210516&format=tar.gz&prefix=xenserver-hwdata-20210516#/xenserver-hwdata.tar.gz) = fb289fa479f77c4b4533bdcd2c9193ed8920f9d1


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
