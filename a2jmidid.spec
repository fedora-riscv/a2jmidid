Summary:	Daemon for exposing ALSA sequencer applications in JACK MIDI system
Name:		a2jmidid
Version:	6
Release:	3%{?dist}
URL:		http://home.gna.org/a2jmidid/
Source0:	http://download.gna.org/%{name}/%{name}-%{version}.tar.bz2
# Fix DSO linking error
# https://gna.org/support/index.php?2547
Patch0:		a2jmidid-linking.patch
# a2jmidi_bridge.c and j2amidi_bridge.c are GPLv2+
# The rest is GPLv2
License:	GPLv2 and GPLv2+
Group:		Applications/Multimedia
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

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
%patch0 -p1 -b .linking

%build
export CFLAGS="%{optflags}"
./waf configure --prefix=%{_prefix} \
	--enable-pkg-config-dbus-service-dir
./waf %{?_smp_mflags} -v

%install
rm -fr %{buildroot}
./waf --destdir=%{buildroot} -v	install

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS README gpl2.txt NEWS
%{_bindir}/a2j
%{_bindir}/%{name}
%{_bindir}/a2j_control
%{_bindir}/a2jmidi_bridge
%{_bindir}/j2amidi_bridge
%{_datadir}/dbus-1/services/org.gna.home.a2jmidid.service

%changelog
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