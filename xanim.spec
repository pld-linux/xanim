Summary:	Viewer for various animated graphic formats
Summary(pl):	Przegl±darka do ró¿nych formatów animacji
Name:		xanim
Version:	2801
Release:	2
Epoch:		1
License:	Free for non-commercial distribution
Group:		X11/Applications/Graphics
# 2801 at http://smurfland.cit.buffalo.edu/xanim/files/
# new version at ftp://ftp.ayamura.org/pub/graphics/xanim2920.tar.gz
Source0:	ftp://xanim.va.pubnix.com/%{name}%{version}.tar.gz
# Source0-md5: e2ecd086c160f18dd7cc3cac438758c2
# old dlls at http://smurfland.cit.buffalo.edu/xanim/dlls/
Source1:	ftp://xanim.va.pubnix.com/dlls/vid_cvid_2.0_linuxELFx86g21.tgz
# Source1-md5: 258efcea057a758433f24cecb10c6c7b
Source2:	ftp://xanim.va.pubnix.com/dlls/vid_cyuv_1.0_linuxELFx86g21.tgz
# Source2-md5: 62d169be1c12c7210ac328a29e504d4f
Source3:	ftp://xanim.va.pubnix.com/dlls/vid_h261_1.0_linuxELFx86g21.tgz
# Source3-md5: 713c2432a1ef1862dad6a6e5083d0d94
Source4:	ftp://xanim.va.pubnix.com/dlls/vid_h263_1.0_linuxELFx86g21.tgz
# Source4-md5: a24bb03c55726bc534028523b0cde320
Source5:	ftp://xanim.va.pubnix.com/dlls/vid_iv32_2.1_linuxELFx86g21.tgz
# Source5-md5: dfe61336160e4ef7f4fcf101716788b3
Source6:	ftp://xanim.va.pubnix.com/dlls/vid_iv41_1.0_linuxELFx86g21.tgz
# Source6-md5: 967afb00d08aadb6496976eaece0b67f
Source7:	ftp://xanim.va.pubnix.com/dlls/vid_iv50_1.0_linuxELFx86g21.tgz
# Source7-md5: a129e01459d12ce2af0be33b14eda5f3
Patch0:		%{name}-modsdir.patch
Patch1:		%{name}-include.patch
# NXDOMAIN
#URL:		http://xanim.va.pubnix.com/home.html
# old homepage, but working
URL:		http://smurfland.cit.buffalo.edu/xanim/home.html
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
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
%{__make} \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/xanim}

install xanim $RPM_BUILD_ROOT%{_bindir}/xanim
%ifarch %{ix86}
install *.xa $RPM_BUILD_ROOT%{_libdir}/xanim
%endif

install docs/xanim.man $RPM_BUILD_ROOT%{_mandir}/man1/xanim.1x

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/* README
%attr(755,root,root) %{_bindir}/*
%ifarch %{ix86}
%dir %{_libdir}/xanim
%attr(755,root,root) %{_libdir}/%{name}/*
%endif
%{_mandir}/man1/*
