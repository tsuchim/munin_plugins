%define date %(echo `date +%Y%m%d`)
Name: munin-plugin-local
Version: 0.1.%{date}
Release: 1%{?dist}
Summary: Munin local plugins

License: GPL
URL: https://github.com/tsuchim
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

%description
Munin local files

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/munin/
cp -r /usr/local/share/munin/* %{buildroot}/usr/share/munin/

%files
%defattr(-,root,root,-)
/usr/share/munin/*

%changelog