Summary:	Viewer for various animated graphic formats
Summary(pl):	Przegl±darka do ró¿nych formatów animacji
Name:		xanim
Version:	2801
Release:	2
License:	Free for Non-commercial distribution
Epoch:		1
Group:		X11/Applications/Graphics
Source0:	ftp://xanim.va.pubnix.com/%{name}%{version}.tar.gz
Source1:	ftp://xanim.va.pubnix.com/dlls/vid_cvid_2.0_linuxELFx86g21.tgz
Source2:	ftp://xanim.va.pubnix.com/dlls/vid_cyuv_1.0_linuxELFx86g21.tgz
Source3:	ftp://xanim.va.pubnix.com/dlls/vid_h261_1.0_linuxELFx86g21.tgz
Source4:	ftp://xanim.va.pubnix.com/dlls/vid_h263_1.0_linuxELFx86g21.tgz
Source5:	ftp://xanim.va.pubnix.com/dlls/vid_iv32_2.1_linuxELFx86g21.tgz
Source6:	ftp://xanim.va.pubnix.com/dlls/vid_iv41_1.0_linuxELFx86g21.tgz
Source7:	ftp://xanim.va.pubnix.com/dlls/vid_iv50_1.0_linuxELFx86g21.tgz
Patch0:		%{name}-modsdir.patch
Patch1:		%{name}-include.patch
URL:		http://xanim.va.pubnix.com/home.html
BuildRequires:	zlib-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Viewer for various animated graphic formats, including QuickTime and
FLiC.

%description -l pl
Przegl±darka do ró¿nych formatów animacji, w tym QuickTime i FLiC.

%prep
%ifarch %{ix86}
%setup -q -n %{name}%{version} -a1 -a2 -a3 -a4 -a5 -a6 -a7
%else
%setup -q -n %{name}%{version}
%endif
%patch0 -p1
%patch1 -p1

%build
xmkmf -a
ln -sf  docs/xanim.man .
%{__make} CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/xanim}

install xanim $RPM_BUILD_ROOT%{_bindir}/xanim
%ifarch %{ix86}
install *.xa $RPM_BUILD_ROOT%{_libdir}/xanim
%endif

install docs/xanim.man $RPM_BUILD_ROOT%{_mandir}/man1/xanim.1x

gzip -9nf docs/* README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc  README.gz docs/{*.doc,*.readme,README*,proptest.c}.gz
%attr(755,root,root) %{_bindir}/*
%ifarch %{ix86}
%dir %{_libdir}/xanim
%attr(755,root,root) %{_libdir}/%{name}/*
%endif
%{_mandir}/man1/*
