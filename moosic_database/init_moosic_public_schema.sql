/* Moosic : Mood - Music recommendation
 * 
 * Team : Rythm Byte engineers 
 * 
 * 
 * DDL 
 * table data definition
 */


-- search path to moosic schema
-- moosic_schema = public??
-- SET csv_data_path = moosic-project;


-- Load and import data
	-- load csv files from local data directory / online source
    -- create tables if it doesn't exist
    -- then drop table




-- DROP SCHEMA public;

CREATE SCHEMA public AUTHORIZATION pg_database_owner;

-- public.affect_vad_coords definition
-- Drop table

-- DROP TABLE public.affect_vad_coords;

CREATE TABLE public.affect_vad_coords (
	english_word text NULL,
	valence float4 NULL,
	energy float4 NULL,
	dominance float4 NULL
);

-- Permissions

ALTER TABLE public.affect_vad_coords OWNER TO postgres;
GRANT ALL ON TABLE public.affect_vad_coords TO postgres;


-- public.artist_spotify_data definition

-- Drop table

-- DROP TABLE public.artist_spotify_data;

CREATE TABLE public.artist_spotify_data (
	id text NULL,
	followers float4 NULL,
	genres text NULL,
	"name" text NULL,
	popularity int4 NULL
);

-- Permissions

ALTER TABLE public.artist_spotify_data OWNER TO postgres;
GRANT ALL ON TABLE public.artist_spotify_data TO postgres;


-- public.moodsic_data definition

-- Drop table

-- DROP TABLE public.moodsic_data;

CREATE TABLE public.moodsic_data (
	artists_id text NULL,
	track_id text NULL,
	artist_name text NULL,
	track_name text NULL,
	genres text NULL,
	release_date text NULL,
	explicit int4 NULL,
	duration_ms int4 NULL,
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
	time_signature int4 NULL,
	followers int4 NULL,
	artist_popularity int4 NULL,
	track_popularity int4 NULL,
	main_genres text NULL,
	core_genres text NULL,
	mood_42d_label text NULL,
	mood_1d_label text NULL,
	mood_goal text NULL,
	blues int4 NULL,
	classical int4 NULL,
	country int4 NULL,
	disco int4 NULL,
	dubstep int4 NULL,
	edm int4 NULL,
	electronic int4 NULL,
	folk int4 NULL,
	funk int4 NULL,
	gospel int4 NULL,
	"hip hop" int4 NULL,
	house int4 NULL,
	"indie rock" int4 NULL,
	jazz int4 NULL,
	metal int4 NULL,
	other int4 NULL,
	pop int4 NULL,
	"punk rock" int4 NULL,
	"r&b" int4 NULL,
	reggae int4 NULL,
	rock int4 NULL,
	rockabilly int4 NULL,
	soul int4 NULL,
	techno int4 NULL
);

-- Permissions

ALTER TABLE public.moodsic_data OWNER TO postgres;
GRANT ALL ON TABLE public.moodsic_data TO postgres;


-- public.moosic_data_processed definition

-- Drop table

-- DROP TABLE public.moosic_data_processed;

CREATE TABLE public.moosic_data_processed (
	artists_id varchar(50) NULL,
	track_id text NULL,
	artist_name text NULL,
	track_name text NULL,
	genres text NULL,
	release_date text NULL,
	explicit int4 NULL,
	duration_ms int4 NULL,
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
	time_signature int4 NULL,
	followers int4 NULL,
	artist_popularity int4 NULL,
	track_popularity int4 NULL,
	main_genres text NULL,
	core_genres text NULL,
	mood_goal text NULL
);

-- Permissions

ALTER TABLE public.moosic_data_processed OWNER TO postgres;
GRANT ALL ON TABLE public.moosic_data_processed TO postgres;


-- public.spotify_data definition

-- Drop table

-- DROP TABLE public.spotify_data;

CREATE TABLE public.spotify_data (
	track_id text NULL,
	track_name text NULL,
	track_popularity int4 NULL,
	track_duration_ms int4 NULL,
	track_explicit int4 NULL,
	track_artists_name text NULL,
	track_id_artists text NULL,
	track_release_date text NULL,
	track_danceability float4 NULL,
	track_energy float4 NULL,
	track_key int4 NULL,
	track_loudness float4 NULL,
	track_mode int4 NULL,
	track_speechiness float4 NULL,
	track_acousticness float4 NULL,
	track_instrumentalness float4 NULL,
	track_liveness float4 NULL,
	track_valence float4 NULL,
	track_tempo float4 NULL,
	track_time_signature int4 NULL,
	artist_id text NULL,
	artist_name text NULL,
	artist_genres text NULL,
	artist_followers float4 NULL,
	artist_popularity int4 NULL
);

-- Permissions

ALTER TABLE public.spotify_data OWNER TO postgres;
GRANT ALL ON TABLE public.spotify_data TO postgres;


-- public.track_spotify_data definition

-- Drop table

-- DROP TABLE public.track_spotify_data;

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

-- Permissions

ALTER TABLE public.track_spotify_data OWNER TO postgres;
GRANT ALL ON TABLE public.track_spotify_data TO postgres;


-- public.valence_lexicon definition

-- Drop table

-- DROP TABLE public.valence_lexicon;

CREATE TABLE public.valence_lexicon (
	mood_label text NULL,
	valence float4 NULL
);

-- Permissions

ALTER TABLE public.valence_lexicon OWNER TO postgres;
GRANT ALL ON TABLE public.valence_lexicon TO postgres;



CREATE OR REPLACE FUNCTION public.load_csv_file(target_table text, csv_path text, col_count integer)
 RETURNS void
 LANGUAGE plpgsql
AS $function$

declare

iter integer; -- dummy integer to iterate columns with
col text; -- variable to keep the column name at each iteration
col_first text; -- first column name, e.g., top left corner on a csv file or spreadsheet

begin
    create table temp_table ();

    -- add just enough number of columns
    for iter in 1..col_count
    loop
        execute format('alter table temp_table add column col_%s text;', iter);
    end loop;

    -- copy the data from csv file
    execute format('copy temp_table from %L with delimiter '','' quote ''"'' csv ', csv_path);

    iter := 1;
    col_first := (select col_1 from temp_table limit 1);

    -- update the column names based on the first row which has the column names
    for col in execute format('select unnest(string_to_array(trim(temp_table::text, ''()''), '','')) from temp_table where col_1 = %L', col_first)
    loop
        execute format('alter table temp_table rename column col_%s to %s', iter, col);
        iter := iter + 1;
    end loop;

    -- delete the columns row
    execute format('delete from temp_table where %s = %L', col_first, col_first);

    -- change the temp table name to the name given as parameter, if not blank
    if length(target_table) > 0 then
        execute format('alter table temp_table rename to %I', target_table);
    end if;

end;

$function$
;

-- Permissions

ALTER FUNCTION public.load_csv_file(text, text, int4) OWNER TO postgres;
GRANT ALL ON FUNCTION public.load_csv_file(text, text, int4) TO postgres;


-- Permissions

GRANT ALL ON SCHEMA public TO pg_database_owner;
GRANT USAGE ON SCHEMA public TO public;




