#
# Conditional build:
%bcond_without	instantclient	# build against Oracle instantclient

Summary:	Library to access Oracle databases
Summary(pl.UTF-8):	Biblioteka dostępu do baz danych Oracle
Name:		libsqlora8
Version:	2.3.3
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://www.poitschke.de/libsqlora8/%{name}-%{version}.tar.gz
# Source0-md5:	1fcb146f795bddad6baf2916b322c168
Patch0:		%{name}-format.patch
URL:		http://www.poitschke.de/libsqlora8/
%{?with_instantclient:BuildRequires:	oracle-instantclient-devel >= 8}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libsqlora8 is simple C-library to access Oracle databases via the OCI
interface.

%description -l pl.UTF-8
libsqlora8 jest prostą biblioteką C umożliwiającą dostęp do baz danych
Oracle przez interfejs OCI.

%package devel
Summary:	Header files for libsqlora8 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libsqlora8
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libsqlora8 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libsqlora8.

%package static
Summary:	Static libsqlora8 library
Summary(pl.UTF-8):	Statyczna biblioteka libsqlora8
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsqlora8 library.

%description static -l pl.UTF-8
Statyczna biblioteka libsqlora8.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--enable-sqlora1 \
%if %{with instantclient}
	ORACLE_CPPFLAGS="-I/usr/include/oracle/client" \
	--with-oraclehome=/usr \
	--with-oraversion=10.0 \
%else
	--with-oraclehome=$ORACLE_HOME \
%endif
	--with-threads=posix

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# nothing arch-dependent (assuming same OS)
%{__mv} $RPM_BUILD_ROOT%{_libdir}/%{name}/include/%{name}-config.h $RPM_BUILD_ROOT%{_includedir}

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsqlora8.la
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/packages/libsqlora8

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS NEWS-2.2
%attr(755,root,root) %{_libdir}/libsqlora8-2.3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsqlora8-2.3.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/html/*.{css,html,png}
%attr(755,root,root) %{_bindir}/libsqlora8-config
%attr(755,root,root) %{_libdir}/libsqlora8.so
%{_includedir}/libsqlora8-config.h
%{_includedir}/sqlora.h
%{_pkgconfigdir}/libsqlora8.pc
%{_aclocaldir}/aclibsqlora8.m4
%{_aclocaldir}/acoracle.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libsqlora8.a
