PRAGMA foreign_keys = ON;

CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY,
    team_name TEXT NOT NULL UNIQUE
);

CREATE TABLE agents (
    agent_id INTEGER PRIMARY KEY,
    agent_code TEXT NOT NULL UNIQUE,
    team_id INTEGER NOT NULL,
    active INTEGER NOT NULL CHECK (active IN (0,1)),
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

CREATE TABLE tickets (
    ticket_id INTEGER PRIMARY KEY,
    ticket_code TEXT NOT NULL UNIQUE,
    agent_id INTEGER NOT NULL,
    channel TEXT NOT NULL CHECK (channel IN ('Email','Phone','Chat','Web')),
    priority TEXT NOT NULL CHECK (priority IN ('Low','Medium','High','Critical')),
    category TEXT NOT NULL CHECK (category IN ('Billing','Technical','Delivery','Account','General')),
    opened_at TEXT NOT NULL,
    due_at TEXT NOT NULL,
    resolved_at TEXT,
    status TEXT NOT NULL CHECK (status IN ('Open','In Progress','Resolved')),
    csat INTEGER CHECK (csat BETWEEN 1 AND 5),
    FOREIGN KEY (agent_id) REFERENCES agents(agent_id)
);
