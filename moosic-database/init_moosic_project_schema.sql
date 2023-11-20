/* Moosic : Mood - Music recommendation
 * 
 * Team : Rythm Byte engineers 
 * 
 * 
 * DDL 
 * table data definition
 */


-- search path to moosic schema
-- moosic_schema = moosic-project ?? 
-- SET csv_data_path = moosic-project;


-- Load and import data
	-- load csv files from local data directory / online source
    -- create tables if it doesn't exist
    -- then drop table





-- DROP SCHEMA "moosic-project";

CREATE SCHEMA "moosic-project" AUTHORIZATION postgres;
-- "moosic-project".moodsic_data definition

-- Drop table

-- DROP TABLE "moosic-project".moodsic_data;

CREATE TABLE "moosic-project".moodsic_data (
	artists_id text NULL,
	track_id text NULL,
	artist_name text NULL,
	track_name text NULL,
	genres text NULL,
	release_date text NULL,
	explicit int8 NULL,
	duration_ms int8 NULL,
	danceability float8 NULL,
	energy float8 NULL,
	"key" int8 NULL,
	loudness float8 NULL,
	"mode" int8 NULL,
	speechiness float8 NULL,
	acousticness float8 NULL,
	instrumentalness float8 NULL,
	liveness float8 NULL,
	valence float8 NULL,
	tempo float8 NULL,
	time_signature int8 NULL,
	followers int8 NULL,
	artist_popularity int8 NULL,
	track_popularity int8 NULL,
	main_genres text NULL,
	core_genres text NULL,
	mood_goal text NULL
);

-- Permissions

ALTER TABLE "moosic-project".moodsic_data OWNER TO postgres;
GRANT ALL ON TABLE "moosic-project".moodsic_data TO postgres;



CREATE OR REPLACE FUNCTION "moosic-project".get_csv_file(csv_file_path text)
 RETURNS void
 LANGUAGE plpgsql
AS $function$
BEGIN
    -- Extract table name from CSV file path
    -- Assuming the CSV file name is the same as the table name
    -- You may need to adjust this logic if your file names are different
    -- E.g., '/path/to/folder/your_table_name.csv' => 'your_table_name'
    DECLARE
        table_name text := regexp_replace(csv_file_path, '.*/([^/]+)\.csv', '\1');
        sql_statement text;
    BEGIN
        -- Create a generic table if it doesn't exist
        EXECUTE format('CREATE TABLE IF NOT EXISTS "moosic-project".%I ();', table_name);
        
        -- Generate the COPY command to import data
        sql_statement := format('\COPY "moosic-project".%I FROM %L WITH CSV HEADER', table_name, csv_file_path);
        
        -- Execute the COPY command
        EXECUTE sql_statement;
        
        RAISE NOTICE 'Data from % imported into %', csv_file_path, table_name;
    END;
END;
$function$
;

-- Permissions

ALTER FUNCTION "moosic-project".get_csv_file(text) OWNER TO postgres;
GRANT ALL ON FUNCTION "moosic-project".get_csv_file(text) TO postgres;

CREATE OR REPLACE FUNCTION "moosic-project".import_csv_files()
 RETURNS void
 LANGUAGE plpgsql
AS $function$
DECLARE 
    csv_files text[] := ARRAY[
        '/Users/graceeze/Documents/data_practitioner_repos/mood_music_recommendation_system/data/moosic-raw/spotify_600k_tracks.csv', 
        '/Users/graceeze/Documents/data_practitioner_repos/mood_music_recommendation_system/data/moosic-raw/spotify_600k_artists.csv',
        '/Users/graceeze/Documents/data_practitioner_repos/mood_music_recommendation_system/data/processed/moodsic_data.csv',
        '/Users/graceeze/Documents/data_practitioner_repos/mood_music_recommendation_system/data/processed/valence_lexicon.csv',
        '/Users/graceeze/Documents/data_practitioner_repos/mood_music_recommendation_system/data/processed/affect_VAD_coords.csv'
    ];
    csv_file text;
    data_table_name text;
    table_name_check text;
BEGIN 
    -- Loop through and import CSV files
    FOREACH csv_file IN ARRAY csv_files
    LOOP 
        data_table_name :=  csv_file; --regexp_replace(csv_file, '.*/(.*).csv', '\1');
        table_name_check := data_table_name;
   
        -- Check if the table exists; if not, create it
        IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = 'moosic-project' AND table_name = table_name_check) THEN
            EXECUTE format('CREATE TABLE "moosic-project".%I ();', data_table_name);
            RAISE NOTICE 'Table % created', data_table_name;
        END IF;

        -- Use the COPY command to import data from the CSV file into the table
        -- EXECUTE format('COPY "moosic-project".%I FROM %L WITH DELIMITER '','' CSV HEADER', data_table_name, csv_file);
		EXECUTE format('\copy "moosic-project".%I FROM %L WITH CSV HEADER', data_table_name, csv_file);

        RAISE NOTICE 'Data from % imported into %', csv_file, data_table_name;
    END LOOP; 
END;
$function$
;

-- Permissions

ALTER FUNCTION "moosic-project".import_csv_files() OWNER TO postgres;
GRANT ALL ON FUNCTION "moosic-project".import_csv_files() TO postgres;

CREATE OR REPLACE FUNCTION "moosic-project".import_csv_files1()
 RETURNS void
 LANGUAGE plpgsql
AS $function$
DECLARE 
    csv_files text[] := ARRAY[
        '/Users/graceeze/Documents/data_practitioner_repos/mood_music_recommendation_system/data/moosic-raw/spotify_600k_tracks.csv', 
        '/Users/graceeze/Documents/data_practitioner_repos/mood_music_recommendation_system/data/moosic-raw/spotify_600k_artists.csv',
        '/Users/graceeze/Documents/data_practitioner_repos/mood_music_recommendation_system/data/processed/moodsic_data.csv',
        '/Users/graceeze/Documents/data_practitioner_repos/mood_music_recommendation_system/data/processed/valence_lexicon.csv',
        '/Users/graceeze/Documents/data_practitioner_repos/mood_music_recommendation_system/data/processed/affect_VAD_coords.csv'
    ];
    csv_file text;
    data_table_name text;
    table_name_check text;
    i integer; -- Counter for the loop
BEGIN 
    -- Loop through and import CSV files
    FOR i IN 1..array_length(csv_files, 1)
    LOOP 
        csv_file := csv_files[i];
        data_table_name := regexp_replace(csv_file, '.*/(.*).csv', '\1');
        table_name_check := data_table_name;
   
        -- Check if the table exists; if not, create it
        IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = 'moosic-project' AND table_name = table_name_check) THEN
            EXECUTE format('CREATE TABLE "moosic-project"."%I" ();', data_table_name);
            RAISE NOTICE 'Table % created', data_table_name;
        END IF;

        -- Use the COPY command to import data from the CSV file into the table
        EXECUTE format('\COPY "moosic-project"."%I" FROM %L WITH DELIMITER '','' CSV HEADER', data_table_name, csv_file);

        RAISE NOTICE 'Data from % imported into %', csv_file, data_table_name;
    END LOOP; 
END;
$function$
;

-- Permissions

ALTER FUNCTION "moosic-project".import_csv_files1() OWNER TO postgres;
GRANT ALL ON FUNCTION "moosic-project".import_csv_files1() TO postgres;


-- Permissions

GRANT ALL ON SCHEMA "moosic-project" TO postgres;








