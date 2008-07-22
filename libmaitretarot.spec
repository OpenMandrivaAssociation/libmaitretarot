%define name libmaitretarot
%define version 0.1.98
%define release %mkrel 11
%define major 0
%define libname %mklibname maitretarot %major
%define libnamedevel %mklibname -d maitretarot

Summary: The Maitretarot library
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Games/Cards
Source: http://www.nongnu.org/download/maitretarot/devel.pkg/%{version}/%{name}-%{version}.tar.bz2
URL: http://www.nongnu.org/maitretarot/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: glib2-devel
BuildRequires: libxml2-devel

%description
Maitretarot is a tarot server game. Libmaitretarot is a library for
both the server and any client.

%description -l fr
Maitretarot est le serveur pour un jeu de tarot. Libmaitretarot 
est une biblothèque pour à la fois le serveur et n'importe quel client.

%package -n %libname
Summary: The Maitretarot library
Group: System/Libraries
Provides: %name = %version-%release

%description -n %libname
Maitretarot is a tarot server game. Libmaitretarot is a library
for both the server and any client.

%description -n %libname -l fr
Maitretarot est le serveur pour un jeu de tarot. Libmaitretarot
est une biblothèque pour à la fois le serveur et n'importe quel client.

%package -n %libnamedevel
Summary: Development files from Libmaitretarot
Group: System/Libraries
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %{_lib}%{name}0-devel

%description -n %libnamedevel
This package is need to build application wich use Libmaitretarot.

%description -n %libnamedevel -l fr
Ce package est utilisé pour compiler les applications qui utilise 
Libmaitretarot.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog 
%{_libdir}/*.so.*

%files -n %libnamedevel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/maitretarot.h

