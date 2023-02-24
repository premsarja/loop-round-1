report_part_1 = """SELECT cte.store_id,
  cte.time_zone,
  cte.status,
  st.time_stamp,
  sh.day_of_week,
  sh.start_time_local,
  sh.end_time_local
FROM(
  SELECT s.store_id,
    MAX(s.time_zone_str) time_zone,
    ss.status
  FROM store s
    INNER JOIN store_status ss ON ss.store_id = s.store_id
  GROUP BY s.store_id,
    ss.status
) cte
LEFT JOIN (
  SELECT store_id,
    status,
    MAX(timestamp) time_stamp
  FROM store_status
  GROUP BY store_id, status
) st ON st.store_id = cte.store_id 
	AND st.status = cte.status
LEFT JOIN store_hours sh ON sh.store_id = cte.store_id
  AND sh.day_of_week = (SELECT extract(isodow FROM date (st.time_stamp)) - 1)
ORDER BY cte.store_id;
"""
