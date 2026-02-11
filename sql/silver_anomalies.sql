-- Identificando 'Location Hopping' em Salvador
CREATE TABLE IF NOT EXISTS silver_alerts AS
WITH
    spatial_check AS (
        SELECT
            client_id,
            neighborhood,
            timestamp,
            amount,
            LAG(neighborhood) OVER (
                PARTITION BY
                    client_id
                ORDER BY timestamp
            ) AS prev_neighborhood,
            LAG(timestamp) OVER (
                PARTITION BY
                    client_id
                ORDER BY timestamp
            ) AS prev_timestamp
        FROM bronze_transactions
    )
SELECT
    *,
    CASE
        WHEN neighborhood <> prev_neighborhood
        AND (
            strftime ('%s', timestamp) - strftime ('%s', prev_timestamp)
        ) < 600 THEN 'Suspect: Location Hop'
        WHEN amount > 4000 THEN 'Critical: High Value'
        ELSE 'Normal'
    END AS anomaly_flag
FROM spatial_check;
