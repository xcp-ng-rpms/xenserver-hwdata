Name: xenserver-hwdata
Summary: Additional hardware identification and configuration data
Version: 20170101
Release: 1.xs6%{dist}
License: GPLv2+
Group: System Environment/Base
Source: https://code.citrite.net/rest/archive/latest/projects/XS/repos/xs-hwdata/archive?at=v%{version}&format=tar.gz&prefix=%{name}-%{version}#/%{name}.tar.gz

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: hwdata

%description
Additional (more up-to-date) hardware identification and configuration data.

%prep
%autosetup -p1 -n xenserver-hwdata-20170101

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
