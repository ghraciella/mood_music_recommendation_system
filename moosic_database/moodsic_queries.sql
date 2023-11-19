
/* Moosic : Mood - Music recommendation
 * 
 * Team : Rythm Byte engineers 
 * 
 * 
 */


----
----

-- affect lexicon with valence, energy values


SELECT
	*
FROM
    public.affect_vad_coords avc 
WHERE
    english_word  = 'relaxed';

-- relaxed, valence = 0.865, energy = 0.090, dominance = 0.320



SELECT
	*
FROM
    public.affect_vad_coords avc 
WHERE
    english_word  = 'overwhelming';

-- overwhelming, valence = 0.327, energy = 0830, dominance = 0.640


SELECT
	*
FROM
    public.valence_lexicon vl 
WHERE
    mood_label  = 'overwhelming';

-- overwhelming, valence = 0.32
      

   
   
--- ...
--- ...

-- join all tables in the spotify schema and query all data from it


--- create table 'spotify_data' with changed names

--CREATE TABLE public.merged_spotify_dataset AS
--       SELECT *
--       FROM
--           public.track_spotify_data AS t
--       LEFT JOIN
--            public.artist_spotify_data AS a
--       ON
--          t.id_artists = a.id;


--- create table 'spotify_data' with changed names

CREATE TABLE public.spotify_data AS
	SELECT t.id AS track_id,
	         t.name AS track_name,
	         t.popularity AS track_popularity,
	         t.duration_ms AS track_duration_ms,
	         t.explicit AS track_explicit,
	         t.artists AS track_artists_name,
	         t.id_artists AS track_id_artists,
	         t.release_date AS track_release_date,
	         t.danceability AS track_danceability,
	         t.energy AS track_energy,
	         t.key AS track_key,
	         t.loudness AS track_loudness,
	         t.mode AS track_mode,
	         t.speechiness AS track_speechiness,
	         t.acousticness AS track_acousticness,
	         t.instrumentalness AS track_instrumentalness,
	         t.liveness AS track_liveness,
	         t.valence AS track_valence,
	         t.tempo AS track_tempo,
	         t.time_signature AS track_time_signature,
	         a.id AS artist_id,
	         a.name AS artist_name,
	         a.genres AS artist_genres,
	         a.followers AS artist_followers,
	         a.popularity AS artist_popularity
					
	     FROM
	         public.track_spotify_data AS t
	     LEFT JOIN
	         public.artist_spotify_data AS a
	     ON
	        t.id_artists = a.id;




-- query spotify combined data
    
	       
SELECT *
FROM public.spotify_data;	       
	       

SELECT count(*) 
FROM public.spotify_data;

-- 586,672


-- query tracks based on release date

SELECT
    track_name,
    track_release_date
FROM
    public.spotify_data
WHERE
    track_release_date BETWEEN '2004-01-01' AND '2012-06-30';



-- query spotify data where valence are energy are in certain threshold
-- low valence, low energy  

SELECT
    track_id,
    track_name,
	track_artists_name,    
    track_valence ,
    track_energy 
FROM
    public.spotify_data
WHERE
    track_valence IN (0.0, 0.5)
    AND track_energy IN (0.0, 0.5);
   
   
SELECT
	count(*) 
FROM
    public.spotify_data
WHERE
    track_valence IN (0.0, 0.5)
    AND track_energy IN (0.0, 0.5);

-- 33
   

-- low valence, high energy  

SELECT
    track_id,
    track_name,
	track_artists_name,    
    track_valence ,
    track_energy 
FROM
    public.spotify_data
WHERE
    track_valence IN (0.0, 0.5)
    AND track_energy IN (0.5, 1.0);

SELECT
	count(*) 
FROM
    public.spotify_data
WHERE
    track_valence IN (0.0, 0.5)
    AND track_energy IN (0.5, 1.0);


-- 

SELECT
	count(*)
FROM
    public.spotify_data
WHERE
    track_valence IN (0.75,1.0)
    AND track_energy  IN (0.5, 0.75);
   
-- ....
-- ....
   
   



----
----


-- query specific columns
SELECT  track_id, artist_name,
			energy, valence,
			core_genres , mood_goal 
FROM public.moodsic_data;



-- sort

SELECT track_id, artist_name, 
		energy, valence, 
		core_genres, mood_goal
FROM public.moodsic_data
GROUP BY track_id, artist_name, energy, valence, core_genres, mood_goal;


-- check if data is balanced based on the moods
SELECT  count(*)
FROM public.moodsic_data
GROUP BY  mood_goal;



-- query all columns and group by core genre count and mood goal 

SELECT  count(*)
FROM public.moodsic_data
GROUP BY core_genres , mood_goal;



SELECT  mood_goal , core_genres ,  count(*)
FROM public.moodsic_data
GROUP BY core_genres , mood_goal;


---

SELECT
	count(*)
FROM
    public.moodsic_data
WHERE
    mood_goal = 'relaxed';

-- 11,879


---
--- 
   
-- average valence-energy for music tracks for each mood category 

SELECT
    mood_goal,
    AVG(energy) AS avg_energy,
    AVG(valence) AS avg_valence
FROM
    public.moodsic_data
GROUP BY
    mood_goal
ORDER BY
    mood_goal;
   
/*   
  
|mood_goal|avg_energy|avg_valence|
|---------|----------|-----------|
|angry|0.6130006733802906|0.33264924657054173|
|calm|0.17827775057318812|0.6503684652133646|
|depressed|0.3759731458352164|0.30204353071824475|
|euphoric|0.8579131241287885|0.7483084437391334|
|happy|0.6310432697749417|0.7499549626671853|
|relaxed|0.3966125094867513|0.7053923732113061|
|sad|0.15340699280724948|0.25914204058276025|
|tense|0.8796954290996708|0.33328266863060185|

*/
   
  

-- average valence-energy for music tracks in each genre for each mood category 

SELECT
    mood_goal,
    core_genres,
    AVG(energy) AS avg_energy,
    AVG(valence) AS avg_valence
FROM
    public.moodsic_data
GROUP BY
    mood_goal,
    core_genres
ORDER BY
    mood_goal,
    core_genres;









