Summary:    	Vis5d weather visualizing system.
Summary(pl):	Vis5d Program do wizualizacji zmian pogody.
Name:      	vis5d
Version:   	5.0
Release:   	2
Copyright: 	GPL
Group:     	X11/Applications
Group(pl): 	X11/Aplikacje
Source:    	ftp://iris.ssec.wisc.edu/pub/vis5d-5.0/%{name}-%{version}.tar.Z
Source1:   	ftp://iris.ssec.wisc.edu/pub/vis5d-5.0/%{name}-data.tar.Z
Source2:   	http://www.ssec.wisc.edu/~billh/api50.html
Source3:   	http://www.ssec.wisc.edu/~billh/script50.html
URL:       	http://www.ssec.wisc.edu/~billh/vis5d.html
Patch:     	vis5d-gets-fix.patch
Buildroot: 	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description
Vis5D is a software system for visualizing data made by numerical weather
models and similar sources.  Vis5D works on data in the form of a five-
dimensional rectangle.

%description -l pl
Program do wizualizacji zmian pogody.

%package data
Summary:     Vis5d - sample data.
Summary(pl): Vis5d - przykladowe dane.
Group:     X11/Applications
Group(pl): X11/Aplikacje
Requires: %{name} = %{version}

%description data 
Sample data.

%description -l pl data
Przyk³adowe dane.

%package devel
Summary:     Vis5d development information.
Summary(pl): Vis5d - informacje dla programistów. 
Group:     Development
Group(pl): Programowanie
Requires: %name = %version

%description devel
Vis5d development information.
API and script info.

%description -l pl devel 
Informacje potrzebne do tworzenia aplikacji wspó³pracuj±cych z programem Vis5d.

%prep
%setup -q
%patch  -b .fix

%setup -q -D -T -c data -a 1

%build
make CFLAGS=$RPM_OTP_FLAGS clean
make CFLAGS=$RPM_OTP_FLAGS linux-x

%install
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_libdir}/vis5d/data
install -d $RPM_BUILD_ROOT%{_libdir}/vis5d/sample
install -d $RPM_BUILD_ROOT/usr/doc/%name-%version

install comp_to_v5d $RPM_BUILD_ROOT%{_bindir}
install topoinfo $RPM_BUILD_ROOT%{_bindir}
install v5d* $RPM_BUILD_ROOT%{_bindir}
install vis5d $RPM_BUILD_ROOT%{_bindir}
strip $RPM_BUILD_ROOT%{_bindir}/* ||

install listfonts $RPM_BUILD_ROOT%{_bindir}
install *.tcl $RPM_BUILD_ROOT%{_libdir}/vis5d/sample
install OUT* $RPM_BUILD_ROOT%{_libdir}/vis5d/data
install *.v5d $RPM_BUILD_ROOT%{_libdir}/vis5d/data
install *.TOPO $RPM_BUILD_ROOT%{_libdir}/vis5d/data
install $RPM_SOURCE_DIR/api50.html $RPM_BUILD_ROOT/usr/doc/vis5d-5.0/
install $RPM_SOURCE_DIR/script50.html $RPM_BUILD_ROOT/usr/doc/vis5d-5.0/
install README $RPM_BUILD_ROOT/usr/doc/vis5d-5.0/
install README.ps $RPM_BUILD_ROOT/usr/doc/vis5d-5.0/
install NOTICE $RPM_BUILD_ROOT/usr/doc/vis5d-5.0/
install PORTING $RPM_BUILD_ROOT/usr/doc/vis5d-5.0/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%attr(644, root, root) /usr/doc/vis5d-5.0/PORTING 
%attr(644, root, root) /usr/doc/vis5d-5.0/README 
%attr(644, root, root) /usr/doc/vis5d-5.0/NOTICE 
%attr(755, root, root) %{_bindir}/*

%files data
%attr(644, root, root) %{_libdir}/vis5d/data/*
%attr(644, root, root) %{_libdir}/vis5d/sample/*

%files devel
%attr(644, root, root) /usr/doc/vis5d-5.0/README.ps
%attr(644, root, root) /usr/doc/vis5d-5.0/api50.html 
%attr(644, root, root) /usr/doc/vis5d-5.0/script50.html
