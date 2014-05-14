%define		_state		stable
%define		orgname		klettres

Summary:	K Desktop Environment - Helps child to learn alphabet and to read some syllables
Summary(pl.UTF-8):	K Desktop Environment - Pomoc w nauce alfabetu i sylab dla dzieci
Name:		kde4-klettres
Version:	4.13.1
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	33cb9152f976bd41fa23c2120bcffc65
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel
Obsoletes:	kde4-kdeedu-klettres < 4.6.99
Obsoletes:	klettres <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KLettres is a very simple application that helps a child or an adult
to learn the alphabet and some simple sounds in his own language or in
another language. The program picks up a letter or a syllable in
random, this letter/syllable is displayed and the sound is played. The
user should then type this letter or syllable. Training is done in the
levels where the letter/syllable is not displayed, only the sound is
played. The user does not need to know how to use the mouse, the
keyboard only is needed.

There are five languages available at the moment: Czech, Danish,
Dutch, French and Slovak.

%description -l pl.UTF-8
KLettres to bardzo prosta aplikacja pomagająca dzieciom i dorosłym w
nauce alfabetu i głosek we własnym lub obcym języku. Program losuje
literę lub sylabę, a następnie wyświetla ją i odgrywa dźwięk.
Użytkownik powinien następnie wpisać tę literę lub sylabę. Do ćwiczeń
służą poziomy, gdzie litera/sylaba nie jest wyświetlana, jedynie
dźwięk jest odgrywany. Użytkownik nie musi wiedzieć, jak używać myszy,
wymagana jest tylko klawiatura.

Aktualnie dostępne jest pięć języków: czeski, duński, holenderski,
francuski i słowacki.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klettres
%{_datadir}/apps/klettres
%{_datadir}/config.kcfg/klettres.kcfg
%{_datadir}/config/klettres.knsrc
%{_desktopdir}/kde4/klettres.desktop
%{_iconsdir}/hicolor/scalable/apps/klettres.svgz
%{_iconsdir}/hicolor/*x*/apps/klettres.png
