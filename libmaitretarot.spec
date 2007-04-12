%define name libmaitretarot
%define version 0.1.98
%define release %mkrel 7
%define major 0
%define libname %mklibname maitretarot %major

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

%package -n %libname-devel
Summary: Development files from Libmaitretarot
Group: System/Libraries
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release

%description -n %libname-devel
This package is need to build application wich use Libmaitretarot.

%description -n %libname-devel -l fr
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

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog 
%{_libdir}/*.so.*

%files -n %libname-devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/maitretarot.h



