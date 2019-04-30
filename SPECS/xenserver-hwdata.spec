Name: xenserver-hwdata
Summary: Additional hardware identification and configuration data
Version: 20190202
Release: 1%{?dist}
License: GPLv2+
Group: System Environment/Base

Source0: https://code.citrite.net/rest/archive/latest/projects/XS/repos/xs-hwdata/archive?at=v20190202&format=tar.gz&prefix=xenserver-hwdata-20190202#/xenserver-hwdata.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XS/repos/xs-hwdata/archive?at=v20190202&format=tar.gz&prefix=xenserver-hwdata-20190202#/xenserver-hwdata.tar.gz) = c20d8ddf2fe6527562d1912555f7fbc8f8423c93


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
