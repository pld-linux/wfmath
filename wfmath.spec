%define libsuffix -0.3
Summary:	A math library
Summary(pl.UTF-8):	Biblioteka matematyczna
Name:		wfmath
Version:	0.3.4
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/worldforge/%{name}-%{version}.tar.bz2
# Source0-md5:	2c8b85fc637d1f0e3fbe5a659ba67869
URL:		http://www.worldforge.org/dev/eng/libraries/wfmath
BuildRequires:	automake
BuildRequires:	libstdc++-devel >= 2.95.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the WorldForge math library. The primary focus of %{name} is
geometric objects.

%description -l pl.UTF-8
Biblioteka matematyczna WorldForge. Skupia się głównie na obiektach
geometrycznych.

%package devel
Summary:	Header files for WorldForge math library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki matematycznej WorldForge
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 2.95.2

%description devel
Header files for WorldForge math library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki matematycznej WorldForge.

%package static
Summary:	Static WorldForge math library
Summary(pl.UTF-8):	Statyczna biblioteka matematyczne WorldForge
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static WorldForge math library.

%description static -l pl.UTF-8
Statyczna biblioteka matematyczne WorldForge.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}%{libsuffix}
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
