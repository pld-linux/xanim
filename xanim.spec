Summary:	Viewer for various animated graphic formats
Name:		xanim
Version:	2801
Release:	1
License:	Free for Non-commercial distribution
Serial:		1
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source0:	ftp://xanim.va.pubnix.com/%{name}%{version}.tar.gz
Source1:	ftp://xanim.va.pubnix.com/dlls/vid_cvid_2.0_linuxELFx86g21.tgz
Source2:	ftp://xanim.va.pubnix.com/dlls/vid_cyuv_1.0_linuxELFx86g21.tgz
Source3:	ftp://xanim.va.pubnix.com/dlls/vid_h261_1.0_linuxELFx86g21.tgz
Source4:	ftp://xanim.va.pubnix.com/dlls/vid_h263_1.0_linuxELFx86g21.tgz
Source5:	ftp://xanim.va.pubnix.com/dlls/vid_iv32_2.1_linuxELFx86g21.tgz
Source6:	ftp://xanim.va.pubnix.com/dlls/vid_iv41_1.0_linuxELFx86g21.tgz
Source7:	ftp://xanim.va.pubnix.com/dlls/vid_iv50_1.0_linuxELFx86g21.tgz
Patch0:		xanim-modsdir.patch
Patch1:		xanim-include.patch
URL:		http://xanim.va.pubnix.com/home.html
BuildRequires:	zlib-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Viewer for various animated graphic formats, including QuickTime and
FLiC. Compiled for Intel 686 chips on Linux

%prep
%setup -q -n %{name}%{version}
%ifarch %{ix86}
%setup -q -c -T -D -b 1 -n %{name}%{version}
%setup -q -c -T -D -b 2 -n %{name}%{version}
%setup -q -c -T -D -b 3 -n %{name}%{version}
%setup -q -c -T -D -b 4 -n %{name}%{version}
%setup -q -c -T -D -b 5 -n %{name}%{version}
%setup -q -c -T -D -b 6 -n %{name}%{version}
%setup -q -c -T -D -b 7 -n %{name}%{version}
%endif
%patch0 -p1
%patch1 -p1

%build
xmkmf -a
%{__make} CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/xanim}

install -s xanim $RPM_BUILD_ROOT%{_bindir}/xanim
%ifarch %{ix86}
install -s *.xa $RPM_BUILD_ROOT%{_libdir}/xanim/
%endif

install docs/xanim.man $RPM_BUILD_ROOT%{_mandir}/man1/xanim.1x

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* *.readme docs/* README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.readme.gz docs/{*.doc,*.readme,README*,proptest.c}.gz
%attr(755,root,root) %{_bindir}/*
%ifarch %{ix86}
%dir %{_libdir}/xanim
%attr(755,root,root) %{_libdir}/%{name}/*
%endif
%{_mandir}/man1/*
