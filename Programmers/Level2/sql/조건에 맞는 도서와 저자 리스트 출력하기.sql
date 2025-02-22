select
    b.book_id as BOOK_ID,
    a.author_name as AUTHOR_NAME,
    DATE_FORMAT(b.published_date, '%Y-%m-%d') as PUBLISHED_DATE
from BOOK as b JOIN AUTHOR as a ON b.AUTHOR_ID = a.AUTHOR_ID
where b.CATEGORY = '경제'
order by b.published_date asc;