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
Patch:		vis5d-make.patch
URL:       	http://www.ssec.wisc.edu/~billh/vis5d.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6

%description
Vis5D is a software system for visualizing data made by numerical weather
models and similar sources.  Vis5D works on data in the form of a five-
dimensional rectangle.

%description -l pl
Program do wizualizacji zmian pogody.

%package data
Summary:	Vis5d - sample data.
Summary(pl):	Vis5d - przykladowe dane.
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Requires:	%{name} = %{version}

%description data 
Sample data.

%description -l pl data
Przyk³adowe dane.

%package devel
Summary:	Vis5d development information.
Summary(pl):	Vis5d - informacje dla programistów. 
Group:		Development
Group(pl):	Programowanie
Requires:	%{name} = %{version}

%description devel
Vis5d development information.
API and script info.

%description -l pl devel 
Informacje potrzebne do tworzenia aplikacji wspó³pracuj±cych z programem Vis5d.

%prep
%setup -q
%patch -p1

%setup -q -D -T -c data -a 1

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS" clean
%{__make} CFLAGS="$RPM_OPT_FLAGS" linux-x

%install
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/vis5d/{data,sample}}
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}-devel/

install comp_to_v5d $RPM_BUILD_ROOT%{_bindir}
install topoinfo $RPM_BUILD_ROOT%{_bindir}
install v5d* $RPM_BUILD_ROOT%{_bindir}
install vis5d $RPM_BUILD_ROOT%{_bindir}
install listfonts $RPM_BUILD_ROOT%{_bindir}

install *.tcl $RPM_BUILD_ROOT%{_datadir}/vis5d/sample
install OUT* $RPM_BUILD_ROOT%{_datadir}/vis5d/data
install *.v5d $RPM_BUILD_ROOT%{_datadir}/vis5d/data
install *.TOPO $RPM_BUILD_ROOT%{_datadir}/vis5d/data

gzip -9nf README README.ps NOTICE PORTING

strip $RPM_BUILD_ROOT%{_bindir}/* || :

install README.ps.gz $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}-devel/
install %{SOURCE2} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}-devel/
install %{SOURCE3} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}-devel/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc {PORTING,README,NOTICE}.gz
%attr(755, root, root) %{_bindir}/*

%files data
%defattr(644, root, root, 755)
%{_datadir}/vis5d/*

%files devel
%defattr(644, root, root, 755)
%{_docdir}/%{name}-%{version}-devel/README.ps.gz
%{_docdir}/%{name}-%{version}-devel/api50.html 
%{_docdir}/%{name}-%{version}-devel/script50.html
