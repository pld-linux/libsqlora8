Summary:	Library to access Oracle databases
Summary(pl):	Biblioteka dostêpu do baz danych Oracle
Name:		libsqlora8
Version:	2.2.11
Release:	1
License:	free
Vendor:		Kai Poitschke
Group:		Libraries
Source0:	http://www.poitschke.de/libsqlora8/%{name}-%{version}.tar.gz
# Source0-md5:	683f97278a64f4187e0302388102c06f
URL:		http://www.poitschke.de/libsqlora8/
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libsqlora8 is simple C-library to access Oracle databases via the OCI
interface.

%description -l pl
libsqlora8 jest prost± bibliotek± C umo¿liwiaj±c± dostêp do baz danych
Oracle przez interfejs OCI.

%package devel
Summary:	Header files for libsqlora8 library
Summary(pl):	Pliki nag³ówkowe biblioteki libsqlora8
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for libsqlora8 library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libsqlora8.

%package static
Summary:	Static libsqlora8 library
Summary(pl):	Statyczna biblioteka libsqlora8
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libsqlora8 library.

%description static -l pl
Statyczna biblioteka libsqlora8.

%prep
%setup -q

%build
%configure \
	--enable-sqlora1 \
	--with-oraclehome=$ORACLE_HOME
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_aclocaldir},%{_bindir},%{_libdir},%{_includedir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f doc/html/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS NEWS-2.2
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/html
%attr(755,root,root) %{_bindir}/*
#%attr(755,root,root) %{_bindir}/%{name}-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/sqlora.h
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
