Summary:	Daemon for exposing ALSA sequencer applications in JACK MIDI system
Name:		a2jmidid
Version:	8
Release:	12%{?dist}
URL:		http://home.gna.org/a2jmidid/
Source0:	http://download.gna.org/%{name}/%{name}-%{version}.tar.bz2
# a2jmidi_bridge.c and j2amidi_bridge.c are GPLv2+
# The rest is GPLv2
# Fix DSO linking: https://gna.org/support/index.php?2934
Patch0:		a2jmidid-linking.patch
Patch1:		a2jmidid-man.patch
Patch2:		a2jmidid-aarch64.patch
Patch3:		a2jmidid-ppc64.patch
License:	GPLv2 and GPLv2+
Group:		Applications/Multimedia

BuildRequires:	alsa-lib-devel
BuildRequires:	dbus-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	python
Requires:	dbus


%description
a2jmidid is a project that aims to ease usage of legacy ALSA sequencer
applications, in a JACK MIDI enabled system. There are two ways to use legacy
ALSA sequencer applications in JACK MIDI system.

The first approach is to use automatic bridging. For every ALSA sequencer port
you get one JACK MIDI port. If ALSA sequencer port is both input and output
one, you get two JACK MIDI ports, one input and output.

The second approach is to static bridges. You start application that creates
one ALSA sequencer port and one JACK MIDI port. Such bridge is unidirectional.

%prep
%setup -q
%patch0 -p1 -b .dso.linking
%patch1 -p1 -b .man
%patch2 -p1 -b .aarch64
%patch3 -p1 -b .ppc64

%build
export CFLAGS="%{optflags}"
./waf configure --prefix=%{_prefix} \
	--enable-pkg-config-dbus-service-dir
./waf %{?_smp_mflags} -v

%install
./waf --destdir=%{buildroot} -v	install

%files
%doc AUTHORS README gpl2.txt NEWS
%{_bindir}/a2j
%{_bindir}/%{name}
%{_bindir}/a2j_control
%{_bindir}/a2jmidi_bridge
%{_bindir}/j2amidi_bridge
%{_datadir}/dbus-1/services/org.gna.home.a2jmidid.service
%{_mandir}/man1/a2j*
%{_mandir}/man1/j2a*

%changelog
* Thu Feb 16 2017 Orcan Ogetbil <oget [dot] fedora [at] gmail [dot] com> - 8-12
- Add patch to fix build on ppc64*

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Oct 26 2014 Peter Robinson <pbrobinson@fedoraproject.org> 8-8
- Add patch to fix ftbfs on aarch64

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 13 2013 Brendan Jones <brendan.jones.it@gmail.com> 8-3
- Release bump for F19

* Sat Sep 15 2012 Jørn Lomax <northlomax@gmail.com> - 8-2
- added patch for man pages

* Mon Jul 09 2012 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 8-1
- Update to 8.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 7-1
- Update to 7.
- Drop upstreamed patches.

* Fri Jul 16 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 6-3
- Fix license tag

* Wed May 19 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 6-2
- Fix DSO linking

* Sat Jan 30 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 6-1
- Update to 6

* Thu Nov 26 2009 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 5-1
- Initial Fedora package. Specfile borrowed from SuSE.

* Mon Jun 15 2009 Toni Graffy <toni@links2linux.de> - 5-0.pm.1
- update to 5
* Sun Aug 03 2008 Toni Graffy <toni@links2linux.de> - 4-0.pm.1
- update to 4
* Sat Oct 27 2007 Toni Graffy <toni@links2linux.de> - 2-0.pm.1
- update to 2
* Mon Aug 27 2007 Toni Graffy <toni@links2linux.de> - 1-0.pm.1
- Initial build 1
