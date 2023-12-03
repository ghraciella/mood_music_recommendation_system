/* Moosic : Mood - Music recommendation
 * 
 * Team : Rythm Byte engineers 
 * 
 * 
 * DDL 
 * table data definition
 */


-- search path to moosic schema
-- moosic_schema = moosic-project ?? public??
-- SET csv_data_path = moosic-project;


-- Load and import data
	-- load csv files from local data directory / online source
    -- create tables if it doesn't exist
    -- then drop table




-- Artist table creation / definition for spotify music track dataset
CREATE TABLE IF NOT EXISTS public.artist_spotify_data (
	id text NULL,
	followers float4 NULL,
	genres text NULL,
	"name" text NULL,
	popularity int4 NULL
);

-- Rename column names for id and 'name' in artist table
ALTER TABLE public.artist_spotify_data 
RENAME COLUMN id TO artist_id
RENAME COLUMN "name" to artist_name;



-- Permissions artist table

ALTER TABLE public.artist_spotify_data OWNER TO postgres;
GRANT ALL ON TABLE public.artist_spotify_data TO postgres;

-- Drop table
-- DROP TABLE artist_spotify_data;




----------------------------------------------------------------------------
----------------------------------------------------------------------------
----------------------------------------------------------------------------




-- Tracks table creation / definition for spotify music track dataset
CREATE TABLE public.track_spotify_data (
	id text NULL,
	"name" text NULL,
	popularity int4 NULL,
	duration_ms int4 NULL,
	explicit int4 NULL,
	artists text NULL,
	id_artists text NULL,
	release_date text NULL,
	danceability float4 NULL,
	energy float4 NULL,
	"key" int4 NULL,
	loudness float4 NULL,
	"mode" int4 NULL,
	speechiness float4 NULL,
	acousticness float4 NULL,
	instrumentalness float4 NULL,
	liveness float4 NULL,
	valence float4 NULL,
	tempo float4 NULL,
	time_signature int4 NULL
);


-- Delete 
DELETE FROM public.track_spotify_data
WHERE id='' AND "name"='' AND popularity=0 AND duration_ms=0 
    AND explicit=0 AND artists='' AND id_artists='' 
    AND release_date='' AND danceability=0 AND energy=0 
    AND "key"=0 AND loudness=0 AND "mode"=0 AND speechiness=0 AND acousticness=0 
    AND instrumentalness=0 AND liveness=0 AND valence=0 AND tempo=0 AND time_signature=0;


-- Rename column names for id and 'name' in artist table
ALTER TABLE public.track_spotify_data 
RENAME COLUMN id TO track_id
RENAME COLUMN "name" to track_name
RENAME COLUMN artists TO artists_name
RENAME COLUMN id_artists TO artists_id
RENAME COLUMN "key" TO key_pitch
RENAME COLUMN "mode" to mode_scale;



-- Permissions track table
ALTER TABLE public.track_spotify_data OWNER TO postgres;
GRANT ALL ON TABLE public.track_spotify_data TO postgres;

-- Drop table
-- DROP TABLE public.track_spotify_data;




----------------------------------------------------------------------------
----------------------------------------------------------------------------
----------------------------------------------------------------------------


-- Tracks table creation / definition for spotify affect_VAD_lexicon dataset

CREATE TABLE public.affect_vad_coords (
	english_word text NULL,
	valence float4 NULL,
	energy float4 NULL,
	dominance float4 NULL
);

-- Permissions
ALTER TABLE public.affect_vad_coords OWNER TO postgres;
GRANT ALL ON TABLE public.affect_vad_coords TO postgres;


-- Drop table
-- DROP TABLE public.affect_vad_coords;





----------------------------------------------------------------------------
----------------------------------------------------------------------------
----------------------------------------------------------------------------


-- Tracks table creation / definition for spotify valence_lexicon dataset
CREATE TABLE public.valence_lexicon (
	mood_label text NULL,
	valence float4 NULL
);

-- Permissions
ALTER TABLE public.valence_lexicon OWNER TO postgres;
GRANT ALL ON TABLE public.valence_lexicon TO postgres;


-- Drop table
-- DROP TABLE public.affect_vad_coords;






