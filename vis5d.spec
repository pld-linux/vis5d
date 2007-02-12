Summary:	Vis5d weather visualizing system
Summary(pl.UTF-8):	Program do wizualizacji zmian pogody
Name:		vis5d
Version:	5.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	ftp://iris.ssec.wisc.edu/pub/vis5d-5.0/%{name}-%{version}.tar.Z
# Source0-md5:	d8190bfcd4e2b227dbfe0b7ba57a1a8a
Source1:	ftp://iris.ssec.wisc.edu/pub/vis5d-5.0/%{name}-data.tar.Z
# Source1-md5:	01a54cc7e5079dea8432792b037edfdd
Source2:	http://www.ssec.wisc.edu/~billh/api50.html
# Source2-md5:	5d0ff6b843f628a2cea2d8badfdfe9fd
Source3:	http://www.ssec.wisc.edu/~billh/script50.html
# Source3-md5:	26bec0dffb62a5e2e0a1a766b698c10c
Patch0:		%{name}-make.patch
URL:		http://www.ssec.wisc.edu/~billh/vis5d.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Vis5D is a software system for visualizing data made by numerical
weather models and similar sources. Vis5D works on data in the form of
a five- dimensional rectangle.

%description -l pl.UTF-8
Program do wizualizacji zmian pogody.

%package data
Summary:	Vis5d - sample data
Summary(pl.UTF-8):	Vis5d - przykładowe dane
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description data
Sample data.

%description data -l pl.UTF-8
Przykładowe dane.

%package devel
Summary:	Vis5d development information
Summary(pl.UTF-8):	Vis5d - informacje dla programistów
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description devel
Vis5d development information. API and script info.

%description devel -l pl.UTF-8
Informacje potrzebne do tworzenia aplikacji współpracujących z
programem Vis5d.

%prep
%setup -q
%patch0 -p1

%setup -q -D -T -c data -a 1

%build
%{__make} CFLAGS="%{rpmcflags}" clean
%{__make} CFLAGS="%{rpmcflags}" linux-x

%install
rm -rf $RPM_BUILD_ROOT
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

install %{SOURCE2} .
install %{SOURCE3} .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NOTICE PORTING
%attr(755, root, root) %{_bindir}/*

%files data
%defattr(644,root,root,755)
%{_datadir}/vis5d

%files devel
%defattr(644,root,root,755)
%doc README.ps* api50.html script50.html
