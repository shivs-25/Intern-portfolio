CREATE TABLE IF NOT EXISTS categories (
    category_id TEXT PRIMARY KEY,
    category_name TEXT
);

CREATE TABLE IF NOT EXISTS competitions (
    competition_id TEXT PRIMARY KEY,
    competition_name TEXT,
    gender TEXT,
    type TEXT,
    parent_id TEXT,
    category_id TEXT,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

CREATE TABLE IF NOT EXISTS seasons (
    season_id TEXT PRIMARY KEY,
    name TEXT,
    year INTEGER,
    competition_id TEXT,
    FOREIGN KEY (competition_id) REFERENCES competitions(competition_id)
);

CREATE TABLE IF NOT EXISTS competitor_rankings (
    competitor_id TEXT PRIMARY KEY,
    competitor_name TEXT,
    rank INTEGER,
    movement INTEGER,
    points INTEGER,
    competitions_played INTEGER,
    country TEXT,
    country_code TEXT,
    abbreviation TEXT
);
