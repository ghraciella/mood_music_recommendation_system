/* Moosic : Mood - Music recommendation
 * 
 * Team : Rythm Byte engineers 
 * 
 * 
 */


-- search path to moosic schema
-- moosic_schema = moosic-project
SET csv_data_path = moosic-project;


-- Load and import data
	-- loop through csv files in local data directory 
    -- extract the table name from the file name
    -- usage of 'copy' to import data from the files into the tables



DO $$ 
DECLARE 
    csv_file text;
    table_name text;
BEGIN 
    FOR csv_file IN ('/Users/graceeze/Documents/data_practitioner_repos/mood_music_recommendation_system/data/moosic-raw/spotify_600k_tracks.csv', 
					'/Users/graceeze/Documents/data_practitioner_repos/mood_music_recommendation_system/data/moosic-raw/spotify_600k_artists.csv',
					'/Users/graceeze/Documents/data_practitioner_repos/mood_music_recommendation_system/data/processed/moodsic_data.csv',
					'/Users/graceeze/Documents/data_practitioner_repos/mood_music_recommendation_system/data/processed/valence_lexicon.csv',
					'/Users/graceeze/Documents/data_practitioner_repos/mood_music_recommendation_system/data/processed/affect_VAD_coords.csv') 
    LOOP 
        table_name := regexp_replace(csv_file, '.*/(.*).csv', '\1');

        EXECUTE format('COPY %I FROM %L WITH CSV HEADER', table_name, csv_file);

        RAISE NOTICE 'Data from % imported into %', csv_file, table_name;
    END LOOP; 
END $$;












