Summary: 	Viewer for various animated graphic formats
Name: 		xanim
Version: 	2800
Release: 	1
Copyright: 	Free for Non-commercial distribution
Group: 		X11/Applications/Graphics
Source0: 	ftp://xanim.va.pubnix.com/xanim2800.tar.gz
Source1: 	ftp://xanim.va.pubnix.com/modules/xa1.0_cyuv_linuxELF.o.Z
Source2: 	ftp://xanim.va.pubnix.com/modules/xa2.0_cvid_linuxELF.o.Z
Source3: 	ftp://xanim.va.pubnix.com/modules/xa2.0_iv32_linuxELF.o.Z
#Patch0: patch-xanim27070-ppro-nonfree
URL: 		http://xanim.va.pubnix.com/home.html
BuildRoot: 	/var/tmp/xanim-root

%description
Viewer for various animated graphic formats, including QuickTime and FLiC.
Compiled for Intel 686 chips on Linux

%prep
#%setup -b 0 -q -n xanim27070
%setup -q -n %{name}%{version} 
gunzip <%{SOURCE1}
#%patch0 -p1

%build
xmkmf
make 

%install
install -d ${RPM_BUILD_ROOT}/usr/X11R6/{bin,man/man1}
install xanim ${RPM_BUILD_ROOT}/usr/X11R6/bin/xanim
install docs/xanim.man ${RPM_BUILD_ROOT}/usr/X11R6/man/man1/xanim.1x

gzip -9nf ${RPM_BUILD_ROOT}/usr/X11R6/man/man1/*

%files
%defattr(644,root,root,755)
%attr(755, root, root) /usr/X11R6/bin/*
/usr/X11R6/man/man1/*

%changelog

* Thu Jan 14 1999 Philip Long <plong@mitre.org>
- Adapted Toshio's work for this i686 package. Much of his flexibility has
  been stripped for simplicity.
- This version is very 686 specific due to lack of ./configure
  i.e. -O6 -march=pentiumpro for pgcc-1.1.1
- This version also assumes new linux sound

* Fri Jan 30 1998 Toshio Kuratomi <badger@prtr-13.ucsc.edu>

- Now made with a buildroot!
- Added support for the Radius Cinepak, Intel Indeo, and Creative
  CYUV decompressors.  Because of the licensing, these compressors are
  included as nosrc.  Please note:  I think the cinepak license is such
  that it could be included in the srpm, but I'm not certain so it isn't
  here.
- Made the redhat provided patch0 for linux only.  When someone else builds
  this package, they may have to set up a patch for their OS.
- Added a URL tag.
- Added patch to enable X Multibuffering.
- Upped the optimization levels a bit.

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>

- built against glibc
