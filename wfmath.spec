%define libsuffix -0.3
Summary:	A math library.
Name:		wfmath
Version:	0.3.4
Release:	0.1
License:	GPL
Group:		Libraries
URL:		http://www.worldforge.org/dev/eng/libraries/wfmath
Source0:	http://dl.sourceforge.net/worldforge/%{name}-%{version}.tar.bz2
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the WorldForge math library. The primary focus of %{name} is
geometric objects.

%package devel
Summary:	A math library headers and static libs.
Group:		Development/Libraries
Requires:	%{name} = %{version} libstdc++-devel >= 2.95.2

%description devel
This is the WorldForge math library. The primary focus of %{name} is
geometric objects.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
CXXFLAGS=%{rpmcflags}
%configure --enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*
%doc AUTHORS COPYING NEWS README

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/lib*.a
%{_pkgconfigdir}/*
%{_includedir}/%{name}%{libsuffix}
