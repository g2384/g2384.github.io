File Type Signatures Search
----
<pre>
Description	Extensions	Header	Offset	Footer	Default in KB
JPEG	JPG;jpeg;jpe	\xFF\xD8\xFF[\xDB\xE0\xE1\xE2\xE8\xEB\xEE\xFE\xC4]	0
PNG	png	\x89PNG\x0D\x0A\x1A\x0A	0	\x49\x45\x4E\x44\xAE\x42\x60\x82
GIF	gif	GIF8[79]a	0
TIFF/NEF/CR2/DNG	TIF;tiff;nef;cr2;dng	(\x49\x49\x2A\x00)|(\x4D\x4D\x00\x2A)	0
MSO Document Image	mdi	EP\*\x00	0
MS Windows Journal	jnt;jtp	NB\x2A\x00	0
Bitmap	bmp;dib	BM.....\x00.\x00....[\x0C\x28\x6C\x7C]\x00	0
AOL ART	art	\x4A\x47[\x03\x04]\x0E\x00\x00\x00	0
PC Paintbrush	pcx	\x0A\x05\x01\x08	0
Paint Shop Pro	psp;PsPImage	(Paint Shop Pro I)|(~BK\x00)	0
High Dynamic Range	hdr	\#\?RADIANCE	0
Canon RAW	crw	HEAPCCDR	6
Adobe Photoshop	psd	8BPS\x00\x01\x00\x00\x00\x00\x00\x00	0
Graphics Metafile	wmf	(\xD7\xCD\xC6\x9A)|([\x01\x02]\x00\x09\x00)	0
Enhanced Metafile	emf	 EMF\x00\x00\x01\x00	40
thumbcache	db	CMMM	0
Corel Photopaint	cpt	CPT[789]?FILE	0
Corel Draw	cdr	CDR	8
Corel Binary Metafile	cmx	CMX1	8
CAD	dwg	AC10	0
Rich Text Format	rtf	\{\\rtf	0
HTML/XML	HTML;htm;phtml;shtml;xml;xsd;msc	([\x0D\x0A\x09\x20]{0,9}((<[hH][tT][mM][lL])|(<![dD][oO][cC][tT][yY][pP])|(<!--)|(<\?xml)|(<xs:schema)))|(\xEF\xBB\xBF\x3C)|(\xFF\xFE\x3C\x00)	0
PHP	php;php3;php4	<\?php	0
Internet Explorer cache	dat	Client UrlCache 	0
AOL PFC	pfc;org	AOLVM100	0
Mailbox	mbox;mbs	From 	0
Outlook	pst;ost;fdb	!BDN	0
Outlook Express	dbx	\xCF\xAD\x12\xFE	0
OS X Tiger E-mail	emlx	#{3,7}\x0D?\x0A(Delivered-To|Status|Return-Path|From|To|Date|Message-Id):\x20	0	</plist>\x0A	128
Outlook 2011 Mac	olk14MsgSource	MSrc	0
OE addr. book	wab	\x9C\xCB\xCB\x8D\x13\x75\xD2\x11\x91\x58\x00\xC0\x4F\x79\x56\xA4	0
OE addr. book (Win95)	wab	\x81\x32\x84\xC1\x85\x05\xD0\x11\xB2\x90\x00\xAA\x00\x3C\xF6\x76	0
vCard	vcf	BEGIN:VCARD	0	END:VCARD	1
Virtual Calendar File	vcs;ics	BEGIN:[vV]C[aA][lL][eE][nN][dD][aA][rR]	0
MS Office/OLE2	ole2;doc;xls;dot;ppt;xla;ppa;pps;pot;msi;sdw;db;vsd;msg	\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1	0
MS Office 2007	docx;xlsx;pptx	_Types\]\.xml	38
MS Access	mdb;mda;mde;mdt;fdb	Standard J	4
MS Access 2007	accdb	\x00\x01\x00\x00Standard ACE DB	0
MS Money	mny	\x00\x01\x00\x00MSISAM	0
SQLite 2.x database	SQLITE2;sqlite;;	\*\* This file contains an SQLite 2\.#	0
SQLite 3.x database	SQLITE3;sqlite;kexi;;	SQLite format 3\x00	0
KWord	kwd	KOffice application/x-kword	10
RagTime Document	rtd	\x43\x23\x2B\x44\xA4\x43\x4D\xA5\x48\x64\x72	0
WordPerfect	wpd;wp;wp5;wp6;wpp	\xFFWPC	0
MS Write	wri	\x31\xBE\x00\x00\x00\xAB\x00\x00\x00\x00\x00\x00	0
MS Write	wri	\x32\xBE\x00\x00\x00\xAB\x00\x00\x00\x00\x00\x00	0
MS OneNote	one	\xE4\x52\x5C\x7B\x8C\xD8\xA7\x4D\xAE\xB1\x53\x78\xD0\x29\x96\xD3	0
OpenOffice Writer	sxw;sxg	sun\.xml\.writer	54
OpenOffice Calc	sxc;stc	sun\.xml\.calc	54
OpenOffice Math	sxm	sun\.xml\.math	54
OpenOffice Impress	sxi	sun\.xml\.impress	54
OpenOffice Draw	sxd;std	sun\.xml\.draw	54
OpenOffice 2 Writer	ott	document\.text-templ	64
OpenOffice 2 Writer	odt	document\.text	64
OpenOffice 2 Calc	ots	document\.spreadsheet-templ	64
OpenOffice 2 Calc	ods	document\.spreads	64
OpenOffice 2 Base	odb	vnd\.sun\.xml\.base	50
OpenOffice 2 Draw	odg	document\.graphic	64
OpenOffice 2 Math	odf	document\.formula	64
OpenOffice 2 Impress	odp	document\.present	64
Quattro Pro Notebook 6.0	wb2	\x00\x00\x02\x00\x02\x10\xC9\x00\x02\x00\x00\x06	0
PostScript/Adobe	ps;eps;ai	%!PS-Adobe	0
Adobe Acrobat	pdf	%PDF\x2D1\x2E	0
Adobe FrameMaker	fm	<MakerFile	0
Quicken	qdf	\xAC\x9E\xBD\x8F	0
Quicken	qsd	QW Ver\. 	0
QuickBooks Backup	qbb	\x45\x86\x00\x00\x06\x00	0
Sage	sly;srt;slt	\x53\x52\x01\x00	0
Lotus WordPro v9	lwp	WordPro	0
Lotus Ami Pro	ami;sam	\[ver\]	0
Lotus 123 v9	123	\x00\x00\x1A\x00\x05\x10\x04	0
Lotus 123 v3-5	wk3;wk4;wk5	\x00\x00\x1A\x00[\x00\x02]\x10\x04\x00	0
Lotus 123 v1	wk1	\x20\x00\x60\x40\x60	0
Lotus Notes	nsf;ntf	\x1A\x00\x00[\x03\x04]\x00\x00	0
Zip Archive	zip;jar;xps	(PK\x03\x04)|(PK00)|(PK\x05\x06)	0
Jar Archive	jar	\x5F\x27\xA8\x89	0
RAR Archive	rar	Rar!\x1a\x07\x00	0
Tar/PAX Archive	tar;pax	ustar	257
KGB Archive	kgb	KGB_arch -	0
GZip Archive	gz;tgz	\x1F\x8B\x08[\x00\x08]....[\x00\x02\x04][\x00-\x12\xFF]	0
BZip Archive	bz2	BZ[0h]#\x31\x41\x59\x26	0
ARJ Archive	arj	\x60\xEA......\x10\x00\x02	0
7-Zip Archive	7z	7z\xBC\xAF\x27	0
Mac Stuffit Self-Extracting Archive	sea	APPLaust!	65
ACE Archive	ace	\*\*ACE\*\*	7
BinHex 4.0	hqx	must be converted with BinHex	11
PList (XML)	plist	<!DOCTYPE plist	39	</plist>\x0A
PList (binary)	plist	bplist00	0
OS X Keychain	keychain	kych	0
Skype chat dbb	dbb	l33l	0
Skype chat dat	dat	sCdB	0
Virtual HD	vhd	conectix	0
Ghost Image	gho;ghs	\xFE\xEF\x01[\x00-\x03]....[\x00\x01][\x00\x01]	0
Acronis True Image file	tib	\xB4\x6E\x68\x44	0
Nero CD Compilation	nri;nrb	\x0E\x4E\x65\x72\x6F\x49\x53\x4F\x30	0	\x00LFDU[^\x00]*
Alcohol 120% CD Image	mdf	\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x02\x00\x01	0
Wave	wav	WAVEfmt 	8
MP3 ID3 v2/3/4	mp3	ID3[\x02-\x04]\x00[\x00\x80]\x00	0
OGG Vorbis	ogg;ogv	OggS\x00	0
Audacity	au	dns\.\x5c	0
AVI	avi	AVI LIST	8		10000
4X Movie	4xm	4XMVLIST	8
Windows Media	asf;wmv;wma;dvr-ms	\x30\x26\xB2\x75\x8E\x66\xCF\x11\xA6\xD9\x00\xAA\x00\x62\xCE\x6C	0		10000
MediaPlayer Playlist	wpl	<\?wpl version=	0
Real Audio	ram;ra	\.ra�	0
Real Media	rm;rmvb;rv	\.RMF	0		10000
QuickTime Movie	mov	moov	4		10000
QuickTime MOV	mov	ftypqt  	4
QuickTime 3GP	3gp	ftypisom	4
QuickTime 3GP	3gp	ftyp3gp	4
QuickTime 3GP	3gp	ftypmmp4	4
QuickTime 3G2	3g2	ftyp3g2a	4
QuickTime M4A	m4a;m4p	ftypM4A\x20	4
QuickTime M4V	m4v	ftypM4V\x20	4
QuickTime MP4	mp4	ftypmp41	4
QuickTime MP4	mp4;m4b	ftypmp42	4
Matroska	mkv;mka	matroska	8
Flash Video	flv	FLV\x01\x05	0		10000
Flash MP4 video	fv4	ftyppf4v	4
MIDI	mid	MThd	0		250
Win9x Registry Hive	registry	CREG	0
WinNT Registry Hive	registry	regf	0
Windows Password	pwl	\xE3\x82\x85\x96	0
Windows Event Log	evt	\x30\x00\x00\x00LfLe	0
Vista Event Logs	evtx	ElfFile	0
EFS Private Key file	EFS;;	\x02\x00\x00\x00\x00\x00\x00\x00[^\x00]\x00\x00\x00.\x00\x00\x00..\x00\x00..\x00\x00..\x00\x00\x14\x00	0		1
EFS Master Key file	EFS;;	\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00[0-9a-f]\x00[0-9a-f]\x00	0		1
Printer Spool 9x	shd	\x4B\x49\x00\x00..\x00\x00..\x00\x00..\x00\x00	0		1
Printer Spool NT	shd	\x66\x49\x00\x00......\x00\x00.\x00\x00\x00	0		1
Printer Spool W2K/XP	shd	\x67\x49\x00\x00.\x00\x00\x00......\x00\x00.\x00\x00\x00	0		4
Printer Spool 2003	shd	\x68\x49\x00\x00.\x00\x00\x00......\x00\x00.\x00\x00\x00	0		4
Printer Spool NT/2K/XP	spl	\x00\x00\x01\x00..\x00\x00\x10\x00\x00\x00..\x00\x00	0
Windows Pagedump	dmp	PAGEDUMP	0
Windows Pagedump	dmp	PAGEDU64	0
Heap dump file	hdmp	MDMP	0
NTFS $LogFile	$LOGFILE;;	RSTR\x1E\x00\x09\x00	0		65536
Windows Prefetch	pf	[\x11\x17]\x00\x00\x00SCCA	0
Task Scheduler	job	((\x47\x04)|(\x01\x05))\x01\x00................\x46\x00	0		1
Windows Shortcut	lnk	\x4C\x00\x00\x00\x01\x14\x02\x00\x00\x00\x00\x00\xC0\x00\x00\x00\x00\x00\x00\x46	0		3
Internet Shortcut	url	\[InternetShortcut\]	0		1
Internet Shortcut	url	\[DEFAULT\]\x0D\x0ABASEURL	0		1
Change Log	clog;log	\x00\x00\x00\x00\x12\xEF\xCD\xAB	4		64
Ubuntu Trash	trashinfo	\[Trash Info\]\x0A	0
KDE cache	kdecache	7\x0Ahttp://	0
Compiled HTML	chm;chi	ITSF\x03\x00\x00\x00	0
Windows Help	hlp;gid	(\x3F\x5F\x03\x00)|(\x4C\x4E\x02\x00)	0
MS Help 2.0	its;lit	ITOLITLS	0
Windows Exec.	exe;dll;drv;vxd;sys;ocx;vbx;com;fon	MZ.[\x00-\x02].[\x00-\x02]	0
ELF Object	o;ko	\x7FELF\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01	0
ELF Executable	elf	\x7FELF\x01\x01\x01\x00.......\x00\x02	0
ELF Shared Object	so	\x7FELF\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03	0
PGP pubring	pkr;gpg	\x99\x01\xA2\x04	0
PGP secring	skr	\x95\x01\xCF\x04	0
Steganos Safe	sle	ACL[2-5]\x00	0
PGP Safe	pgd	PGPdMAIN\x60\x01\x00	0
MS/MSN MARC archive	mar	MARC\x03	0
Compact Disc Digital Audio (CD-DA) file	cda	RIFF....CDDAfmt	0
Online Metadata Cache	spp	\x1F\x44\xFA\xA0\x8E\xF6\xCC\x4D\x9D\x91\x2C\x2E\xBE\xC0\xBB\x63	0
Windows Television	wtv	\xB7\xD8\x00\x20\x37\x49\xDA\x11\xA6\x4E\x00\x07\xE9\x5E\xAD\x8D	0
$I Recycler	recycler	\x01\x00{7}.....\x00\x00\x00.{7}\x01[C-Z]\x00:\x00	0		1
Event Trace Log	etl	\x00[\x00\x04\x0C\x10\x20\x40\x80][\x00\x01\x02]\x00\x06[\x00\x01]\x01[\x04\x05]..\x00\x00[\x01-\x04\x08]\x00\x00\x00.{7}[\x00\x01](aa|Zb)\x02\x00	104
Dialup	dun	\[Phone\]\x0D\x0A	0	1
Firefox	sessionrestore	\(\{windows:\[\{	0	\}\}\)	96
Auto completion	jsonp	window\.google\.ac\.h\(\[	0	\]\]\)	1
setup info	setupinfo;;	DRBKLBSM	24
</pre>
