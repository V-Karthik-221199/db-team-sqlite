
DELETE FROM MOVIE;

DROP TABLE MOVIE;

CREATE TABLE "MOVIE" (
	"MID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"MOVIE_NAME"	TEXT NOT NULL UNIQUE,
	"RELEASE_DATE"	TEXT
);


DELETE FROM PUBLIC_ARTIST;

DROP TABLE PUBLIC_ARTIST;

CREATE TABLE "PUBLIC_ARTIST" (
	"AID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"ARTIST_NAME"	TEXT NOT NULL UNIQUE,
	"ORIGINAL_NAME" TEXT,
	"DOB"	TEXT,
	"LOCATION"	TEXT,
	"COUNTRY" TEXT,
	"DESCRIPTION" TEXT
);

-- ALTER TABLE PUBLIC_ARTIST ADD COLUMN DESCRIPTION TEXT;


DELETE FROM MOVIE_ARTIST;

DROP TABLE MOVIE_ARTIST;

CREATE TABLE "MOVIE_ARTIST" (
	"MAID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"MOVIE_ID"	TEXT NOT NULL,
	"ARTIST_ID"	INTEGER NOT NULL,
	"ARTIST_ROLE"	TEXT NOT NULL
);

DELETE FROM COARTIST_BUBBLE;

DROP TABLE COARTIST_BUBBLE;

CREATE TABLE "COARTIST_BUBBLE" (
	"CBID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"ARTIST_ID"	TEXT NOT NULL,
	"COARTIST_CATEGORY"	TEXT NOT NULL,
	"COARTIST_ID"	TEXT NOT NULL,
	"BUBBLE_SCORE"	INTEGER NOT NULL
);


DELETE FROM ARTIST_SCORE;

DROP TABLE ARTIST_SCORE;

CREATE TABLE "ARTIST_SCORE" (
	"ASID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"ARTIST_ID"	TEXT NOT NULL,
	"YEAR"	INTEGER NOT NULL,
	"CRITIC_SCORE"	INTEGER NOT NULL,
	"AUDIENCE_SCORE"	INTEGER NOT NULL,
	"BOX_OFFICE_SCORE"	INTEGER NOT NULL
);


