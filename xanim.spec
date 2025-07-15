Summary:	Viewer for various animated graphic formats
Summary(pl.UTF-8):	Przeglądarka do różnych formatów animacji
Name:		xanim
Version:	2920
Release:	1
Epoch:		1
License:	Free for non-commercial distribution
Group:		X11/Applications/Graphics
# 2801 at http://xanim.polter.net/files/
Source0:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/%{name}%{version}.tar.gz
# Source0-md5:	3613e6256857f7270d39bba8efd3a5dc
Patch0:		%{name}-config.patch
Patch1:		%{name}-include.patch
Patch2:		%{name}-qt-co64.patch
URL:		http://xanim.polter.net/
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-util-gccmakedep
BuildRequires:	xorg-util-imake
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Viewer for various animated graphic formats, including QuickTime and
FLiC.

%description -l pl.UTF-8
Przeglądarka do różnych formatów animacji, w tym QuickTime i FLiC.

%prep
%setup -q -n %{name}%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
xmkmf -a
ln -sf  docs/xanim.man .
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	LD_FLAGS="%{rpmldflags} -rdynamic" \
	USRLIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/xanim}

install xanim $RPM_BUILD_ROOT%{_bindir}/xanim
install docs/xanim.man $RPM_BUILD_ROOT%{_mandir}/man1/xanim.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_bindir}/xanim
%dir %{_libdir}/xanim
%{_mandir}/man1/xanim.1*
