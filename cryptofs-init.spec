Summary:	Encrypted filesystems support for rc-scripts
Summary(pl):	Wsparcie dla szyfrowanych systemów plików do skryptów startowych
Name:		cryptofs-init
Version:	1.4
Release:	1
License:	GPL
Group:		Base
Group(de):	Gründsätzlich
Group(pl):	Podstawowe
Source0:	ftp://ftp.pld.org.pl/software/cryptofs-init/%{name}-%{version}.tar.gz
Requires:	losetup >= 2.11g-3
Requires:	mount
Prereq:		rc-scripts
Prereq:		/sbin/chkconfig
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a set of scripts to provide easy set up and
usage of encrypted filesystems and swap space.

%description -l pl
Ten pakiet zawiera zestaw skryptów zapewniaj±cy ³atwe ustawienie i
u¿ytkowanie szyfrowanych systemów plików oraz plików/partycji wymiany

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf modules.conf cryptofstab.example README

%post
/sbin/chkconfig --add cryptofs

%postun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del cryptofs
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%verify(not size mtime md5) %config(noreplace) %{_sysconfdir}/cryptofstab
%attr(754,root,root) /etc/rc.d/init.d/cryptofs*
