import xml.etree.ElementTree as ET
from sqlalchemy import create_engine


def inital_load_bagdes(file):
    rows = convert_data_from_xml_to_dict(file, 'row')
    badges = [change_badge_keys(row) for row in rows['rows']]
    return badges


def inital_load_posts(file):
    rows = convert_data_from_xml_to_dict(file, 'row')
    posts = [change_posts_keys(row) for row in rows['rows']]
    return posts


def convert_data_from_xml_to_dict(file, element):
    tree = ET.parse(file)
    root = tree.getroot()
    return {'rows': [row.attrib for row in root.iter(element)]}


def change_posts_keys(row):
    data_keys = ["Id", "PostTypeId", "AcceptedAnswerId", "ParentId", "CreationDate", "DeletionDate",
                 "Score", "ViewCount", "OwnerUserId", "OwerDisplayName", "LastEditorUserId",
                 "LastEditorUserName", "LastEditorDate", "LastActivityDate",
                 "AnswerCount", "CommentCount", "ClosedDate", "CommunityOwnedDate"]
    valid_keys = ["id", "post_type_id", "accepted_answer_id", "parent_id", "creation_date", "deletion_date",
                  "score", "view_count", "owner_user_id", "ower_display_name", "last_editor_user_id",
                  "last_editor_user_name", "last_editor_date", "last_activity_date",
                  "answer_count", "comment_count", "closed_date", "community_owned_date"]
    if 'Id' in row:
        row['Id'] = int(row['Id'])
    if 'OwnerUserId' in row:
        row['OwnerUserId'] = int(row['OwnerUserId'])
    else:
        row['OwnerUserId'] = -1
    if 'LastEditorUserId' in row:
        row['LastEditorUserId'] = int(row['LastEditorUserId'])
    else:
        row['LastEditorUserId'] = -1
    if 'AnswerCount' in row:
        row['AnswerCount'] = int(row['AnswerCount'])
    else:
        row['AnswerCount'] = 0
    # for data_key, valid_key in zip(data_keys, valid_keys):
    #     row[valid_key] = row.get(data_key, None)
    #     if data_key in row:
    #         row.pop(data_key)
    return tuple([row.get(data_key, None) for data_key in data_keys])


def change_badge_keys(row):
    data_keys = ["Id", "UserId", "Name", "Date", "Class", "TagBased"]
    if 'Id' in row:
        row['Id'] = int(row['Id'])
    if 'UserId' in row:
        row['UserId'] = int(row['UserId'])
    if 'Class' in row:
        row['Class'] = int(row['Class'])
    # return {'id': row['Id'], 'user_id': row['UserId'], 'name': row['Name'], 'date': row['Date'],
    #         'class_id': row['Class'], 'tag_based': row['TagBased']}
    return tuple([row.get(data_key, None) for data_key in data_keys])


def get_total_answers(badge_name):
    databank = 'sqlite:///data.db'
    conn = create_engine(databank)
    query = "SELECT sum(answer_count) FROM posts JOIN badges on badges.user_id = posts.owner_user_id where badges.name=?"
    res = conn.execute(query, (badge_name,)).fetchone()[0]
    return res
